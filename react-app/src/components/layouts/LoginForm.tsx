import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';
import CustomButton from '../commons/Button';
import Loader from '../commons/Loader';

interface LoginFormState {
  email: string;
  password: string;
  rememberMe: boolean;
}

const LoginForm: React.FC = () => {
  const [formData, setFormData] = useState<LoginFormState>({
    email: '',
    password: '',
    rememberMe: false,
  });
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    
    try {
      // Giả lập gọi API đăng nhập
      //const response = await login(formData.email, formData.password);
      // Xử lý đăng nhập thành công
      //console.log('Login successful', response);
      // Chuyển hướng sau khi đăng nhập
      // window.location.href = '/dashboard';
    } catch (err) {
      setError('Email hoặc mật khẩu không chính xác');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      {error && <Alert variant="danger">{error}</Alert>}
      
      <Form.Group className="mb-3">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Nhập email của bạn"
          required
        />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Mật khẩu</Form.Label>
        <Form.Control
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder="Nhập mật khẩu"
          required
        />
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Check
          type="checkbox"
          name="rememberMe"
          checked={formData.rememberMe}
          onChange={handleChange}
          label="Ghi nhớ đăng nhập"
        />
      </Form.Group>

      <div className="d-grid gap-2 mt-4">
        <CustomButton 
          type="submit" 
          variant="dark" 
          disabled={loading}
          className="btn-lg"
        >
          {loading ? <Loader size="sm" /> : 'Đăng nhập'}
        </CustomButton>
      </div>
    </Form>
  );
};

export default LoginForm;
