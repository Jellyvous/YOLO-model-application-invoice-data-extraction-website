function loadImage(event) {
    const imageBox = document.getElementById('image-box');
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            imageBox.innerHTML = '<img src="' + e.target.result + '" class="img-fluid" />';
        };
        reader.readAsDataURL(file);
    }
}

const form = document.querySelector('form');
const detectImageButton = document.getElementById('detect-button');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    detectImageButton.disabled = true;

    const formData = new FormData(form);
    fetch('/', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        console.log(response);
        response.json();
    })
    .then(data => {
        if (data.extracted_text) {
            displayResults(data.result_data, data.store_name);
        } else if (data.error) {
            console.error('Error:', data.error);
        }
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        detectImageButton.disabled = false;
    });
});

function displayResults(data, storeName) {
    const tableBody = document.querySelector("#resultTable tbody");
    tableBody.innerHTML = ''; 

    if (data && Array.isArray(data)) {
        data.forEach(row => {
            const tr = document.createElement("tr");

            const tdItem = document.createElement("td");
            tdItem.textContent = row.item || "N/A"; 
            tdItem.setAttribute("contenteditable", "true"); 
            tdItem.classList.add("editable"); 

            const tdQuantity = document.createElement("td");
            tdQuantity.textContent = row.quantity || "N/A";  
            tdQuantity.setAttribute("contenteditable", "true"); 
            tdQuantity.classList.add("editable"); 

            const tdPrice = document.createElement("td");
            tdPrice.textContent = row.price ? row.price.toLocaleString() : "N/A";  
            tdPrice.setAttribute("contenteditable", "true"); 
            tdPrice.classList.add("editable");  

            tr.appendChild(tdItem);
            tr.appendChild(tdQuantity);
            tr.appendChild(tdPrice);

            tableBody.appendChild(tr);
        });
    }

    const storeNameElement = document.getElementById("storeName");
    storeNameElement.textContent = storeName || "Unknown Store";  
    storeNameElement.setAttribute("contenteditable", "true");
    storeNameElement.classList.add("editable");
}


function processTextToJSON(text) {
    const lines = text.split('\n');
    const result = [];
    let currentItem = null;

    lines.forEach(line => {
        if (line.startsWith('Item:')) {
            if (currentItem) {
                result.push({ items: [currentItem] });
            }
            currentItem = { item: line.replace('Item: ', '').trim() };
        } else if (line.startsWith('Quantity:')) {
            if (currentItem) {
                currentItem.quantity = line.replace('Quantity: ', '').trim();
            }
        } else if (line.startsWith('Price:')) {
            if (currentItem) {
                currentItem.price = line.replace('Price: ', '').trim();
            }
        } else if (line.startsWith('store_name:')) {
            result.push({ store_name: line.replace('store_name: ', '').trim(), items: [] });
        }
    });

    if (currentItem) {
        result.push({ items: [currentItem] });
    }

    const finalJSON = {
        "results.jpg": result
    };

    return finalJSON;
}

// Generate table data to JSON
function generateTableDataToJSON() {
    const rows = document.querySelectorAll("#resultTable tbody tr");
    const data = [];
    const result = {};
    
    rows.forEach(row => {
        const cells = row.querySelectorAll("td");
        const itemData = {
            item: cells[0].textContent.trim(),
            quantity: parseFloat(cells[1].textContent.trim()) || null,
            price: parseFloat(cells[2].textContent.trim()) || null
        };
        data.push(itemData);
    });
    
    const storeName = document.getElementById("storeName").textContent.trim();
    
    if (storeName) {
        if (!result["results.jpg"]) {
            result["results.jpg"] = [];
        }
    
        result["results.jpg"].unshift({
            store_name: storeName,
            items: data
        });
    }
        
    return result;
}

//Download JSON
function downloadJSON() {
    const jsonData = generateTableDataToJSON();
    
    const jsonString = JSON.stringify(jsonData, null, 2);  
    
    const blob = new Blob([jsonString], { type: "application/json" });
    
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "invoice_data.json";  
    
    link.click();
}


function confirmUpload() {
    const userConfirmed = confirm("Are you sure want to save to your Data?");
    
    if (userConfirmed) {
        const jsonData = generateTableDataToJSON();  

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'  
            },
            body: JSON.stringify(jsonData) 
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server Response:', data);
            alert("Success!");
        })
        .catch(error => {
            console.error('Error uploading JSON:', error);
            alert("There was some error during upload!");
        });
    } else {
        alert("Cancer");
    }
}


