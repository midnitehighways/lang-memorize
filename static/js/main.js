$(document).ready(function() { 

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(function () {  
    $('.header-search-form').on('submit', function(event) {
        var element = $(this)
        event.preventDefault()
        // console.log("form submitted!")  // sanity check
        // console.log($(this).children('.add-example-field').val())
        // console.log($(this).attr("wordid"))        
        var wordid = element.attr("wordid")     // this way we send word.id from HTML to JS
        var example_text = element.children('.add-example-field').val()
        // console.log(wordid + " ---- " + example_text);
        $.ajax({
            url : wordid + "/add-example", // the endpoint
            type : "POST",
            data : {  example_text : example_text, csrfmiddlewaretoken: csrftoken }, // data sent with the post request
            
            // handle a successful response
            success : function(json) {
                element.children('.add-example-field').val('');                     // remove the value from the input
                element.children('.add-example-field').fadeOut(400);
                element.children('.add-example-button').fadeOut(400);
                console.log(json); // log the returned json to the console
                // console.log(element.parent()); // another sanity check
                element.siblings('.add-example').before("<div>" + json.number + ". " + json.example); // insert at the end of examples list

            },
            // handle a non-successful response
            error : function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error 
            }
        });
    })
});

//         // addExample()
//         console.log($(this).children('.add-example-field').val())
//         console.log($(this).attr("wordid"))        // this way we send word.id from HTML to JS
//         var wordid = $(this).attr("wordid")
//         var example_text = $(this).children('.add-example-field').val()
//         console.log(wordid + " ---- " + example_text);

//         $.ajax({
//             url : wordid + "/add-example", // the endpoint
//             type : "POST",
//             data : {  example_text : example_text, csrfmiddlewaretoken: csrftoken }, // data sent with the post request
            
//             // handle a successful response
//             success : function(json) {
//                 $(this).children('.add-example-field').val(''); // remove the value from the input
//                 console.log(json); // log the returned json to the console
//                 console.log("success"); // another sanity check
//             },

//             // handle a non-successful response
//             error : function(xhr,errmsg,err) {
//                 // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                 //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//             }
//         });});    

    

    // $.ajax({
    //     url : "create_post/", // the endpoint
    //     type : "POST", // http method
    //     data : { the_post : $('#post-text').val() }, // data sent with the post request

    //     // handle a successful response
    //     success : function(json) {
    //         $('#post-text').val(''); // remove the value from the input
    //         console.log(json); // log the returned json to the console
    //         console.log("success"); // another sanity check
    //     },

    //     // handle a non-successful response
    //     error : function(xhr,errmsg,err) {
    //         $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
    //             " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
    //         console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    //     }
    // });
    // };

    $(function () {                         
        var element = $('#b');
        element.click(function () {
            $(".info").slideDown("slow").delay(2000).fadeOut(2000);
            // console.log($('.header-right'.siblings));
            // $(".header-right").show().delay(1000).fadeOut();
        }
    )});
    // $('#proba').click(function showInfo() {
    $(".info").slideDown("slow").delay(2000).fadeOut(2000);         // NOTIFICATION!!!!!!!!!!!!!!!!!!!!


    $(function () {                         // FOR TESTING PURPOSES ONLY
        var element = $('.header');
        element.click(function () {
            console.log($('.header-right'.siblings));
            // $(".header-right").show().delay(1000).fadeOut();
        }
    )});

    $("[name=test]").val([testType]);               // set radio button values according to user settings
    $("[name=test_scope]").val([testScope]);
    $("[name=show]").val([showInCommon]);
    
    $("[name=back]").click(function() {
        console.log(this.value+"aaaaaaaaaa");
        $(".wrap").css("background-image", 'url(' + imageURLs[this.value] + ')');
    });
    var imageURLs = ['../static/img/metal4.jpg','../static/img/metallic.jpeg','../static/img/metal2.png','../static/img/metal3.jpg'];
    


    $("#hooray").show().delay(2000).fadeOut();      // show hooray-message and hide it in 2 seconds

    /* Inform user if there're no words in his/her own vocabulary */
    $(function () {
        var element = $('.accordion');      // thus we make sure to load this function only on the certain page
        if (element.length) {               // if there's such element on the page, we're surely on index-page
            if (!$(".each-word").length){   // if there're no words in vocabulary
                // console.log("NO");
                $('#no-words').show();
            }
            // else {console.log("YES");}
        }
    });

    /* Open/close word details */
    $(function () {
        var element = $('.accordion-item-hd');
        element.click(function () {
            var e = $(this).siblings(('.accordion-item-bd'));
            var e2 = $(this).children(('.arrowUp'));
            // console.log(e.children('.edit-word').text());
            e2.toggleClass("arrowDown");
            if(e.is(':hidden')) {
                e.slideDown();
            }
            else { 
            	// if(e.children('.edit-word').text()=="Edit word")
                e.slideUp();
            }
        });
    });

    /* Add example(s) to any word */
    $(function () {
        var element = $('.add-example');
        element.click(function () {
            //var form = $(this).siblings('.add-example-field');	/* siblings help to address the right form in the particular div */
           //console.log($(this).children('.header-search-form').children());
            // console.log($(this).parent().children().children());
            var form = $(this).parent().children().children('.add-example-field');
            var button = form.siblings('.add-example-button');
            if (form.is(':hidden')) {form.show(); button.show(); form.focus();}
            form.animate({'width': form.width() == 100 ? '0px' : '100px'}, 'slow', function () {
                		if (form.width() == 0) {form.hide(); button.hide();}
            });
        });
    });
    
    /* Edit words. Without back-end so far! */
    $(function () {
        var element = $('.edit-word');
        element.click(function () {
            //var form = $(this).siblings('.add-example-field');	/* siblings help to address the right form in the particular div */
           //console.log($(this).children('.header-search-form').children());
            var target = $(this).parent().parent().children('.accordion-item-hd').children('.arrowDown');
            // console.log($(this).parent().parent().children().children());//.children().children());
        	console.log(target);
        	target.siblings().each(
    			function() {
        			if ($(this).find('input').length) {
            			$(this).text($(this).find('input').val());
            			element.text("Edit word");
        			}
        			else {
            			var el_text = $(this).text();
            			if (el_text!='') {		// this way we skip 'text-free' elements, in our case - tools-text-content
            				$(this).html($('<input />',{'value' : el_text}).val(el_text));
            				element.text("Save");
            			}
        			}
    			});
        });
    });

    /* rotate given div using .card class */
    function flip(yes_or_no) {
        $('.result').css('visibility', 'visible');  // show yes-no-button after first click in test. By default it's invisible
        if($('.card').attr('class')==yes_or_no)
            return;
        else
            $('.card').toggleClass('flipped');
    }

    

    ///////////// functions for take-a-test section are below


    function handle_answer(answer)		// check whether answer is correct and react correspondingly
    {
        document.getElementById('asked-word').style.display = "none";
        if(answer == right_answer) {
            // document.getElementById('result').innerHTML = "joo";
            // document.getElementById('result').className = "joo";
            flip('card');           // yes
        }
        else {
            // document.getElementById('result').innerHTML = "ei";
            // document.getElementById('result').className = "ei";
            flip('card flipped');   // no
        }
        if(testType == 'comic') {                           // --- comic
            $("#choices").hide(300); 
        }
        else if(testType == 'classic') {                    // --- classic
            $("#choices").css('visibility', 'hidden');
            $("#choices").hide();
       }
       else {                                               // --- no animation
            $("#choices").hide(0); 
        }
        prepare_test(words);		// now prepare the new test
    }

    $(function () {
        $('.nappi').click(function () {
        	handle_answer($(this).text());
        }
    )})
});             // end of $(document).ready
console.log($('#add-button').siblings());
//the function prepare_test MUST be outside of $(document).ready, since it has to be ready before the page opens for user
function prepare_test(words_list)   // initial function. Determining the 4 words and the asked word using random generation
{
    var maara = words_list.length;              // number of words
    var fin = [];
    var eng = [];

    for(var i = 0; i < maara; i++) {
        // if(userID==words_list[i].fields.user) {
            // console.log(words_list[i].fields.fi);
            fin.push(words_list[i].fields.fi);
            eng.push(words_list[i].fields.en);
        // }
    }
    // if(fin.length >= 4) !!!!!!!!!!!!!!!!!!!!!!!!
    maara = fin.length;         // in case we take into account only OWN words we need to assign maara once again 
    var numbers = [];
    for (var i = 0; i < 4; i++) {                                       // create array numbers[] and populate it with 4 random numbers
        numbers[i] = Math.floor(Math.random( ) * (maara));              // generate these random numbers, each less than 'maara'
        for (var j = i; j > 0; j--) {                                   // check for repetitive numbers in the array
            if (numbers[i] == numbers[j-1]) {                           // if same number found --->
                numbers[i] = Math.floor(Math.random( ) * (maara));      // ----> generate a new one
                i--;
                break;
            }
        }
    }
    var rand = Math.floor(Math.random( ) * 4);                          // the generated number (0..3) defines which word --->
    document.getElementById('asked-word').value = eng[numbers[rand]];   // ---> is going to be asked among the 4 chosen previously
    right_answer = fin[numbers[rand]];                                  // text variable
    ids =  [document.getElementById('choice_1'), document.getElementById('choice_2'), 
            document.getElementById('choice_3'), document.getElementById('choice_4')];
    // for (var i = numbers.length - 1; i > 0; i--) {               // shuffling the numbers-array
    //     var j = Math.floor(Math.random() * (i + 1));
    //     var temp = numbers[i];
    //     numbers[i] = numbers[j];
    //     numbers[j] = temp;
    // }
    
    if(testType == 'comic') {               // --- comic
        $("#asked-word").show(300);
        $("#choices").show(300);
    }
    else if(testType == 'classic') {                                  // --- classic
        $("#choices").css('visibility', 'visible');
        $("#asked-word").fadeIn(600);
        $("#choices").fadeIn(600);
    }
    else {                                  // --- no animation
        $("#asked-word").show(0);
        $("#choices").show(0);
    }

    for (var i = 0; i < 4; i++) {
        ids[i].innerHTML = fin[numbers[i]];     // assigning corresponding words to inputs in "choices"-section
    }
    // $("#asked-word").show(300);
    // $("#choices").show(300);
    
}
///////////////////////////// END OF TAKE-A-TEST SECTION 

/* submit the hidden language form */
function submitLangForm(lang)
{
  
  document.getElementById('selected-lang').value = lang;
  document.langForm.submit();
}









