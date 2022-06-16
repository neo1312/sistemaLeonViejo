window.onload=function(){
//declaracion de variables y constantes
	
const btnOrder= document.getElementById('btnOrderList');
const clientId= document.getElementById('clientId');

//crear nueva orden
btnOrder.addEventListener('click',(e)=>{
	createOrder()
})
    const createOrder = ()=>{
	let client=clientId.value
        let url = "/sale/inicia"
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
		body:JSON.stringify({'id':client})
        })
            .then((response)=>{
                return response.json();
            })
            .then((data)=>{
                console.log('data:',data)
            })
}
}
