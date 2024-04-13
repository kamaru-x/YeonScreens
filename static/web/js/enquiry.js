$(document).ready(function(){
    $('#enq-btn').on('click',function(){
        var name = $('#name').val()
        var email = $('#email').val()
        var number = $('#number').val()
        var message = $('#message').val()
        var service_id = $('#service_id').val()
        var product_id = $('#product_id').val()

        $.ajax({
            'url' : '/enquiry/make/',
            'type' : 'POST',
            'data' : {
                'name':name,'email':email,'number':number,'message':message,'service_id':service_id,'product_id':product_id
            },

            success : function(response){
                if(response.status=='success'){
                    $('#success-message').show()
                }
                $('#enq-form').trigger('reset')
            }
        })
    })
})