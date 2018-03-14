$(document).ready(function(){
  let i=0;
    $("body").keypress(function(){
      i+= 1;
      console.log(i);
      let previous_src=$('#cal').attr('src');
      $('#cal').attr('src','' );
      setTimeout(function(){
        $('#cal').attr('src',previous_src);
      }, 100);

    });
});
