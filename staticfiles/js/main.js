$(function () {
    var element = $('.accordion-item-hd');
    element.click(function () {
        var e = $(this).siblings(('.accordion-item-bd'));
        var e2 = $(this).children(('.arrowUp'));
        e2.toggleClass("arrowDown");
        if(e.is(':hidden')) {
            e.slideDown();
        }
        else { 
        	e.slideUp();
        }
    });
});

$(function () {
    var element = $('.add-example');
    element.click(function () {
        //var form = $(this).siblings('.add-example-field');	/* siblings help to address the right form in the particular div */
       //console.log($(this).children('.header-search-form').children());
        console.log($(this).parent().children().children());
        var form = $(this).parent().children().children('.add-example-field');
        var button = form.siblings('.add-example-button');
        if (form.is(':hidden')) {form.show(); button.show(); form.focus();}
        form.animate({'width': form.width() == 100 ? '0px' : '100px'}, 'slow', function () {
            		if (form.width() == 0) {form.hide(); button.hide();}
        });
    });
});
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

// functions for take-a-test section are below

function prepare_test(words_list)	// initial function. Determining the 4 words and the asked word using random generation
{
    var maara = words_list.length;				// number of words
	var fin = [];
	var eng = [];
	for(var i = 0; i < maara; i++) {
		fin.push(words_list[i].fields.fi);
		eng.push(words_list[i].fields.en);
	}
    var numerot = [];
    for (var i = 0; i < 4; i++) {										// create array numerot[] and populate it with 4 random numbers
        numerot[i] = Math.floor(Math.random( ) * (maara));				// generate these random numbers, each less than 'maara'
        for (var j = i; j > 0; j--) {									// check for repetitive numbers in the array
            if (numerot[i] == numerot[j-1]) {							// if same number found --->
                numerot[i] = Math.floor(Math.random( ) * (maara));		// ----> generate a new one
                i--;
                break;
            }
        }
    }
    var rand = Math.floor(Math.random( ) * 4);							// the generated number (0..3) defines which word --->
    document.getElementById('asked_word').value = eng[numerot[rand]];	// ---> is going to be asked among the 4 chosen previously
    right_answer = fin[numerot[rand]];									// text variable
    ids = [document.getElementById('choice_1'), document.getElementById('choice_2'), document.getElementById('choice_3'), document.getElementById('choice_4')];
    // for (var i = numerot.length - 1; i > 0; i--) {				// shuffling the numerot-array
    //     var j = Math.floor(Math.random() * (i + 1));
    //     var temp = numerot[i];
    //     numerot[i] = numerot[j];
    //     numerot[j] = temp;
    // }
    for (var i = 0; i < 4; i++) {
        ids[i].innerHTML = fin[numerot[i]];		// assigning corresponding words to inputs in "choices"-section
    }
    $("#asked_word").show(300);
    $("#choices").show(300);
}

function handle_answer(answer)		// check whether answer is correct and react correspondingly
{
    document.getElementById('asked_word').style.display = "none";
    if(answer == right_answer) {
        document.getElementById('result').innerHTML = "joo";
        document.getElementById('result').className = "joo";
    }
    else {
        document.getElementById('result').innerHTML = "ei";
        document.getElementById('result').className = "ei";
    }
    $("#choices").hide(300);
    prepare_test(words);		// now prepare the new test
}

$(function () {
    $('.nappi').click(function () {
    	handle_answer($(this).text());
    }
)})
