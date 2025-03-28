import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';

// Import các trang
import Home from './pages/Home';
import Login from './pages/Login';

// const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
//   if (!isAuthenticated()) {
//     return <Navigate to="/login" replace />;
//   }
//   return children;
// };

const AppRoutes: React.FC = () => {
  return (
    <Routes>
      {/* Public routes */}
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      
      {/* Protected routes - thêm khi cần */}
      {/* 
      <Route 
        path="/dashboard" 
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        } 
      />
      */}
      
      {/* Route mặc định khi không tìm thấy trang */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
};

export default AppRoutes;
