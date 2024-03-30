import {Navigate} from "react-router-dom";
import {jwtDecode} from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useState, useEffect} from "react";

// first we are going to check if the user is autorized otherwise redirect them and tell them to login
// before they can view this page
function ProtectedRoute({children}) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    // as soon as we load our ProtecedRoute we ar egoing to try if we have a token
    useEffect(() => {
        auth().catch(() => setIsAuthorized(false)); 
    }, [])
 
    // this will refresh the ACCESS_TOKEN automatically
    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        // get the REFREH_TOKEN and try to send a request to "/api/token/refresh/" route with the "
        // which it should give us a new ACCESS_TOKEN 
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            });
            // if we recived the ACCESS_TOKEN
            if(res.status === 200){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            } else {
                setIsAuthorized(false)
            }

        } catch (error) {
            console.log(error)
            setIsAuthorized(false)
        }
    }

    // this will check if we have to refresh the token or not 
    const auth = async () => {
        // chek if u have the token
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token) {
            setIsAuthorized(false)
            return
        }
        // this decode the value and get access to expiration dates
        const decoded = jwtDecode(token)
        const tokenExpiration = decoded.exp
        // devided by 1000 in order to get the " day " in seconds not in milliseconds
        const now = Date.now() / 1000

        if (tokenExpiration < now) {
            await refreshToken()
        } else {
            setIsAuthorized(true)
        }
    }

    if (isAuthorized === null) {
        // until the state of "isAutorized" is null, we are checking the token or refreshing it  
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to="/login" />

}

export default ProtectedRoute