import React, { useState } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import LoginForm from '../components/layouts/LoginForm';
import SocialLogin from '../components/layouts/SocialLogin';
import Logo from '../components/commons/Logo';

const Login: React.FC = () => {
  return (
    <Container fluid className="login-page d-flex align-items-center justify-content-center">
      <Row className="justify-content-center w-100">
        <Col xs={12} sm={10} md={8} lg={6} xl={4}>
          <Card className="shadow-lg border-0 rounded-lg mt-5">
            <Card.Header className="bg-primary text-white text-center py-4">
              <Logo />
              <h3 className="font-weight-light my-2">Đăng nhập</h3>
            </Card.Header>
            <Card.Body>
              <LoginForm />
              <div className="text-center mt-3">
                <hr className="my-4" />
                <p className="text-muted">Hoặc đăng nhập với</p>
                <SocialLogin />
              </div>
            </Card.Body>
            <Card.Footer className="text-center py-3">
              <div className="small">
                <a href="/register">Chưa có tài khoản? Đăng ký ngay!</a>
              </div>
              <div className="small mt-2">
                <a href="/forgot-password">Quên mật khẩu?</a>
              </div>
            </Card.Footer>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Login;
