function buttonClicked() {
    let btn = document.getElementById('submit-btn');

    let original_btn_text = btn.innerHTML;
    btn.innerHTML = "Thank you, I'll get back to you soon!";

    setTimeout(function() {
        btn.innerHTML = original_btn_text
    }, 5000);
}
