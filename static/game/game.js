function submitUserAnswer(idx) {
    $.ajax({
        type: "POST",
        url: "/update",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(idx),
        success: function(result) {
            console.log(result)
            updateLives(result["lives"])
            updateOnAnswer(idx)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function updateLives(nLives) {
    $("#heart-container").empty()
    for (let i = 0; i < nLives; i++) {
        $("#heart-container").append($(
            `<img src='/static/game/assets/heart.png' />`
        ))
    }
}

function updateOnAnswer(idx) {
    $("#dialogue").text(question.choices[idx].dialogue)

    $(".button-box").empty()
    $(".button-box").append($(
        `<a type="button" class="game-button" href="/game/${question.id + 1}">Continue</a>`
    ))
}


function resetChoices() {
    $.each(question.choices, (i, val) => {
        $(".button-box").append($(
            `<a type="button" class="game-button" data-idx=${i}>${val.text}</a>`
        ))
    })
}

$(document).ready(() => {
    resetChoices()

    $(document).on("click", ".game-button", function() {
        const idx = $(this).data("idx")
        if (idx !== undefined){
            submitUserAnswer(idx)
        }
    })
    $(".game-button")
})
