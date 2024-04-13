$(document).ready(function(){
     // Add feature
     $('#add-feature').on('click', function(){
        $('#features-div').append(
            `<div class="input-group col-span-6 mt-3"> 
                <input name="features[]" type="text" class="form-control" placeholder="Enter Feature Title Here" aria-label="Price" aria-describedby="input-group-price" required>
                <div class="input-group-text feature-delete"><i class="fa-regular fa-trash-can"></i></div>
            </div>`
        );
    });

    // Delete feature
    $('#features-div').on('click', '.feature-delete', function(){
        $(this).closest('.input-group').remove();
    });

    // Add feature
    $('#add-spec').on('click',function(){
        $('#spec-div').append(
            `<div class="input-group col-span-6 mt-3"> 
                <input name="spec-titles[]" type="text" class="form-control" placeholder="Enter Specification Title Here" aria-label="Price" aria-describedby="input-group-price" required>
                <input name="spec-values[]" type="text" class="form-control" placeholder="Enter Specification Value Here" aria-label="Price" aria-describedby="input-group-price" required>
                <div class="input-group-text spec-delete"><i class="fa-regular fa-trash-can"></i></div>
            </div>`
        );
    });

    // Delete feature
    $('#spec-div').on('click', '.spec-delete', function(){
        $(this).closest('.input-group').remove();
    });
});