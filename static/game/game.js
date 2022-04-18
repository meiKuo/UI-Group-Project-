function submitUserAnswer(idx) {
    $.ajax({
        type: "POST",
        url: "/update",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(idx),
        success: function(result) {
            console.log(result)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function updateCurrentState() {
    $.each(question.choices, (i, val) => {
        $(".button-box").append($(
            `<a type="button" class="game-button" data-idx=${i}>${val.text}</a>`
        ))
    })
}

$(document).ready(() => {
    updateCurrentState()


    $(document).on("click", ".game-button", function() {
        const idx = $(this).data("idx")
        if (idx !== undefined){
            submitUserAnswer(idx)
        }
    })
    $(".game-button")
})
