import React from 'react';

interface LogoProps {
  width?: number;
  height?: number;
}

const Logo: React.FC<LogoProps> = ({ width = 120, height = 40 }) => {
  return (
    <div className="logo-container text-center mb-2">
      {/* Thay thế bằng logo thực tế của bạn */}
      <img 
        src="/logo.png" 
        alt="Company Logo" 
        width={width} 
        height={height}
        onError={({ currentTarget }) => {
          currentTarget.onerror = null;
          currentTarget.style.display = 'none';
          currentTarget.parentElement!.innerHTML += '<h2 className="text-primary">Your Logo</h2>';
        }}
      />
    </div>
  );
};

export default Logo;
