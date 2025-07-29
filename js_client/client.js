const loginForm = document.getElementById('login-form');
const baseEnpoint = "http://127.0.0.1:8000/api";
const productList = document.getElementById('product-list');

if(loginForm){

    loginForm.addEventListener('submit', handleLogin)

}

function handleLogin(event){
    event.preventDefault();
    const loginEndpoint = `${baseEnpoint}/token/`;

    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyJsonData = JSON.stringify(loginObjectData)

    const options = {
        method: "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: bodyJsonData
    }

    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response);
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList);
    })
    .catch(err => {
        console.log('err', err);
    })
}


function handleAuthData(authData, callback){

    localStorage.setItem('access', authData.access);
    localStorage.setItem('refresh', authData.access);

    if(callback){
        callback();
    }
}

function writeToContainer(data){
    if(productList){
        productList.innerHTML = "<pre>" + JSON.stringify(data, null,4) + "</pre>";
    }
}

function getProductList(){
    const endpoint = `${baseEnpoint}/create/`;
    const options = {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem('access')}`
        }
    }

    fetch(endpoint, options)
    .then(response=>response.json())
    .then(data=>{

        writeToContainer(data)
    })

}