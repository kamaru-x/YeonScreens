$(document).ready(function(){
    // Add feature on click
    $('#add-feature').on('click', function(){
        $('#features-div').append(
            `<div class="input-group col-span-6 mt-3"> 
                <input name="features[]" type="text" class="form-control" placeholder="Enter Feature Title Here" aria-label="Price" aria-describedby="input-group-price" required>
                <div class="input-group-text feature-delete"><i class="fa-regular fa-trash-can"></i></div>
            </div>`
        );
    });

    // Edit feature on change
    $('.feature-input').on('keyup paste change', function(){
        var feature_id = $(this).data('id');
        var title = $(this).val()
        
        $.ajax({
            'url' : '/dashboard/feature/edit/',
            'type' : 'POST',
            'data' : {'feature_id':feature_id,'title':title},

            success : function(response){
                console.log(response.status)
            } 
        })
    });    

    // Delete feature on click
    $('.feature-delete').on('click', function(){
        var feature_id = $(this).data('id');

        if(feature_id){
            $.ajax({
                'url' : '/dashboard/feature/delete/',
                'type' : 'POST',
                'data' : {'feature_id':feature_id},
    
                success : function(response){
                    console.log(response.status)
                } 
            })
        }

        $(this).closest('.input-group').remove();
    });

    // Add Specification on click
    $('#add-spec').on('click',function(){
        $('#spec-div').append(
            `<div class="input-group col-span-6 mt-3"> 
                <input name="spec-titles[]" type="text" class="form-control" placeholder="Enter Specification Title Here" aria-label="Price" aria-describedby="input-group-price" required>
                <input name="spec-values[]" type="text" class="form-control" placeholder="Enter Specification Value Here" aria-label="Price" aria-describedby="input-group-price" required>
                <div class="input-group-text spec-delete"><i class="fa-regular fa-trash-can"></i></div>
            </div>`
        );
    });

    // Edit Specification on click
    $('.spec-title,.spec-value').on('keyup paste change',function(){
        var spec_id = $(this).data('id')
        var $inputGroup = $(this).closest('.input-group');
        var title = $inputGroup.find('.spec-title').val();
        var value = $inputGroup.find('.spec-value').val();
        
        $.ajax({
            'url' : '/dashboard/spec/edit/',
            'type' : 'POST',
            'data' : {'spec_id':spec_id,'title':title,'value':value},

            success : function(response){
                console.log(response.status)
            } 
        })
    })

    // Delete Specification on click
    $('.spec-delete').on('click',function(){
        var spec_id = $(this).data('id');

        if(spec_id){
            $.ajax({
                'url' : '/dashboard/spec/delete/',
                'type' : 'POST',
                'data' : {'spec_id':spec_id},
    
                success : function(response){
                    console.log(response.status)
                } 
            })
        }

        $(this).closest('.input-group').remove();
    });
});