let curQuestion = 0;

function emptyFields() {

}

function updateCurrentState() {
    const q = questions[curQuestion];

    $("#dialogue").text(q.question)
    $(".button-box").empty()
    $.each(q.choices, (i, val) => {
        $(".button-box").append($(
            `<a type="button" class="game-button" data-idx=${i}>${val.text}</a>`
        ))
    })

    $.post("/game", { id: q.mushroom }, function (data) {
        //img.src = `/static/${data.img_url}`
        console.log(data)
    }, "json")

    console.log(q);
}

$(document).ready(() => {
    updateCurrentState()
})
