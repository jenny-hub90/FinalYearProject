console.log("HDcomments init");
 
const HDC_EL ={
   submit: document.getElementById("hdc_submit"),
   comment: document.getElementById("hdc_comment_input"),
   email: document.getElementById("hdc_email_input"),
   name: document.getElementById("hdc_name_input"),
   reactions:document.getElementsByClassName("hdc_reaction"),
   upvotes:document.getElementsByClassName("hdc_upvote"),
   downvotes:document.getElementsByClassName("hdc_downvote")
};

let canSubmit = false;
let reaction = null;

function hdc_submit(){
    if(canSubmit){
        let comment ={
        comment: HDC_EL.comment.value.trim(),
        email: HDC_EL.email.value.trim(),
        name: HDC_EL.name.value.trim(),
        reaction: reaction
        };
        console.log(comment);
        hdc_disable_submit();
        }
}

function hdc_can_submit(){
    let comment = HDC_EL.comment.value.trim();
    let email = HDC_EL.email.value.trim();
    let name = HDC_EL.name.value.trim();
    if(comment.length > 4 && email.length > 4 && name.length > 4){
        if(hdc_validate_email_Address(email)){
        HDC_EL.submit.classList.add("hdc_submit_enabled");
        HDC_EL.submit.disabled= false;
        canSubmit = true
        console.log("good to go");
        }else{ 
         hdc_disable_submit()
        }
    } else{
      hdc_disable_submit();
    }
}

function hdc_disable_submit(){
    HDC_EL.submit.classList.remove("hdc_submit_enabled");
    HDC_EL.submit.disabled = true;
    canSubmit = false;
}

function hdc_select_reaction(){
   reaction = this.getAttribute("data-reaction");
   let prev = document.getElementsByClassName("hdc_reaction_selected")[0];
   if(prev){
       prev.classList.remove("hdc_reaction_selected");
   }
   this.classList.add("hdc_reaction_selected");
}

function hdc_vote(el, vote){
    if(!el.classList.contains("hdc_vote_disabled")){
    let commentID = el.getAttribute("data-id");
    let score = document.getElementsByClassName("hdc_vote_"+commentID)[0]
    .innerText;
    score = parseInt(score);
    if(vote){
        score = score + 1;
    }else{
        score = score - 1;
    }

    if(score > 0){
        score ='+' + score;
    }
    document.getElementsByClassName(
        "hdc_vote_"+commentID
        )[0].innerText = score;

    el.classList.add("hdc_vote_selected");
    elVotes = document.querySelectorAll(
        "#hdcomment_" + commentID + " .hdc_vote_options span "
    );
    console.log(elVotes)
    for (let i = 0 ; i < elVotes.length; i++){
     elVotes[i].classList.add("hdc_vote_disaled");
    }
}
}

function hdc_set_event_listeners(){
 HDC_EL.submit.addEventListener("click", hdc_submit);
 HDC_EL.comment.addEventListener("keyup",hdc_can_submit);
 HDC_EL.email.addEventListener("keyup",hdc_can_submit);
 HDC_EL.name.addEventListener("keyup",hdc_can_submit);
 for(let i=0; i< HDC_EL.reactions.length; i++){
    HDC_EL.reactions[i].addEventListener("click",hdc_select_reaction);
 }
 for(let i=0; i< HDC_EL.upvotes.length; i++){
    HDC_EL.upvotes[i].addEventListener("click",function(){
     hdc_vote(this, true)
    });
    HDC_EL.downvotes[i].addEventListener("click",function(){
     hdc_vote(this, false)
    });
 }
}
hdc_set_event_listeners();

function hdc_validate_email_Address(email){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
};