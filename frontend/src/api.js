// in here we are going to write the " interceports ".
// The interceports will intercept the request that we are going to send and will automatically add headers 
// so we don't need to manually write it.
// And we are going to use " axios ". 
// Is used for send network requests, preatty easy to use.
// every time we send a request, it will check if we have an access token

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// this is how to pass a JWT token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
)

export default api;