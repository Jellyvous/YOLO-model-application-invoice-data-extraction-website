import axios from 'axios';
import { LoginCredentials, SignupCredentials, AuthResponse } from '../types/Auth';

const API_URL = "https://your-api-url.com/api/auth/";

class AuthService {
    async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await axios.post(API_URL + "signin", credentials);
    if (response.data.token) {
        localStorage.setItem("user", JSON.stringify(response.data));
    }
    return response.data;
    }

    logout(): void {
    localStorage.removeItem("user");
    }

    async register(credentials: SignupCredentials): Promise<any> {
    return axios.post(API_URL + "signup", credentials);
    }

    getCurrentUser(): AuthResponse | null {
    const userStr = localStorage.getItem("user");
    if (userStr) return JSON.parse(userStr);
    return null;
    }
}

export default new AuthService();
