console.log("Welcome to Text Tools website!");

function CopyToClipboard() {
    if (document.selection) {
        let range = document.body.createTextRange();
        range.moveToElementText(document.getElementById("output_text"));
        range.select().createTextRange();
        document.execCommand("copy");
    } else if (window.getSelection) {
        let range = document.createRange();
        range.selectNode(document.getElementById("output_text"));
        window.getSelection().addRange(range);
        document.execCommand("copy");
        // alert("Text has been copied, now paste in the text-area");
    }
}

function CopyToInputBox() {
    let x = document.getElementById("output_text").innerText;
    console.log(x);
    document.getElementById("input_text").innerHTML = x;
}
