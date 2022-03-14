// this is for viewint the whoel details
const buttons = [...document.getElementsByClassName('btnviws')]
const user_name = document.getElementById('id_username')
const user_email = document.getElementById('id_email')
const user_id = document.getElementById('id_user')
const update=document.getElementById('update_form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const alert = document.getElementById('alert')


// this is for active inactice ajax

const active_inactive_array = [...document.getElementsByClassName('active_inactive')]




// this code for hiding the modal 

function hideUpdateModal() {
    $("#update-form-modal").removeClass("in");
    $(".modal-backdrop").remove();
    $('body').removeClass('modal-open');
    $('body').css('padding-right', '');
    $("#update-form-modal").hide();
  }
buttons.forEach(element => {
    const h1=document.getElementById('modalh1')
    const h2=document.getElementById('modalh12')
    element.addEventListener('click',function(){
        $.ajax({
            type:'GET',
            url: `detail/${element.value}/`,
            success:function (response){
                console.log(response)
                h1.innerText=(response.name).slice(0,6)
                h2.innerText = response.email
            },
        })
    })
});

const editbtn = [...document.getElementsByClassName('editbtncls')]

editbtn.forEach(element => {

    element.addEventListener('click',function(){
        $.ajax({
            type:'GET',
            url:`update/${element.value}/`,
            success:function(response){
                user_name.value = response.name
                user_email.value = response.email
                user_id.value = response.id
              

            }
        })




    })   
    
});

update.addEventListener('submit',(e)=>{
    e.preventDefault()
    const name = document.getElementById('id_username').value
    const email = document.getElementById('id_email').value
    const id = document.getElementById('id_user').value

    $.ajax({
        type: 'POST',
        url : `update/${id}/`,
        data:{
            'csrfmiddlewaretoken': csrf[0].value,
            'user_name': name,
            'email': email,
        },
        success: function(response){

            const user_name_change = document.getElementById(`user-${response.id}`)
            const success_h4 = document.getElementById('success_h4')

    
            let name = response.name
            user_name_change.innerText = name.toUpperCase()
            success_h4.innerText = (response.name).slice(0,6)+ " " + 'Updated'
            alert.classList.remove('not_visible')
                
            setTimeout(function(){
                alert.classList.add('not_visible')
                success_h4.innerText= ''
            },3000)
             hideUpdateModal()  
            
        },
        error: function(errors){
            console.log(errors)
        }
    })




})

// this ajax is for active and inactive view

active_inactive_array.forEach(function(element){
    element.addEventListener('click',function(){

        $.ajax({
            type: 'GET',
            url : 'useractivation/',
            data: {
                'id': element.value
            },
            success: function(response) {
                const success_h4 = document.getElementById('success_h4')
                
                alert.classList.remove('not_visible')
                if (response.success){
                    success_h4.style.color ='green'
                    success_h4.textContent = "Activated"

                }
                else{
                    success_h4.style.color ='red'
                    success_h4.textContent = "Inactivated"
                }
                setTimeout(function(){
                    alert.classList.add('not_visible')
                    location.reload()
                },2000)
                
                // location.reload()
                console.log(response)
            },
            error: function(error){
                console.log(error)
            }

        })
    })
})

