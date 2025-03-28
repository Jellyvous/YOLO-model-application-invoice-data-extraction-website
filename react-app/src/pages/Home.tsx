import { Container, Row, Col, Card, Button, Alert, Carousel } from 'react-bootstrap';
import Header from '../components/layouts/Header';
import InvoiceExtraction from '../components/layouts/InvoiceExtraction';

const Home: React.FC = () => {
    return (
        <div>
            <Header></Header>
            <InvoiceExtraction></InvoiceExtraction>
        </div>
    );
}




export default Home;