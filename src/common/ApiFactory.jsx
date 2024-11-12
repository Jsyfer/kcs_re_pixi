import axios from 'axios';
import require_info from '../kcsapi/api_get_member/require_info.json'
import port from '../kcsapi/api_port/port.json'
import getData from '../kcsapi/api_start2/getData.json'

export const post = (url, postData, setResponse) => {
    if (import.meta.env.VITE_USE_MOCK_DATA === "1") {
        setResponse(_get_mock_data(url))
    } else {
        axios.post(url, postData)
            .then(res => {
                setResponse(res.data)
            })
            .catch(error => {
                console.log(error);
            });
    }
}

export const get = (url, setResponse, setLoaded) => {
    if (import.meta.env.VITE_USE_MOCK_DATA === "1") {
        setResponse(_get_mock_data(url))
        if (setLoaded !== undefined) {
            setLoaded(true)
        }
    } else {
        axios.get(url)
            .then(res => {
                setResponse(res.data)
                if (setLoaded !== undefined) {
                    setLoaded(true)
                }
            })
            .catch(error => {
                console.log(error);
            });
    }
}

// use for mock data
const _get_mock_data = (url) => {
    switch (url) {
        case "kcsapi/api_get_member/require_info":
            return require_info
        case "kcsapi/api_port/port":
            return port
        case "kcsapi/api_start2/getData":
            return getData
        default:
            break;
    }
}