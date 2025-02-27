(function ($, Drupal) {

  Drupal.behaviors.initMonacoEditor = {
    attach: function (context, settings) {

      // Check if the settings are available
      if (typeof settings.programiz_pro_challenges === 'undefined') {
        return;
      }

      var codeOutline = settings.programiz_pro_challenges.codeOutline;
      var language = settings.programiz_pro_challenges.language;
      var slug = settings.programiz_pro_challenges.slug;
      var title = settings.programiz_pro_challenges.title;
      var id = settings.programiz_pro_challenges.id;

      $('#programiz-challenge__editor--form', context).once('initMonacoEditor', function () {
        if (window.monaco) {
          initializeMonacoEditor(codeOutline, language);
        } else {
          var config = {
            paths: {
              'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.48.0/min/vs'
            }
          };
          require.config(config);
          require(['vs/editor/editor.main'], function () {
            initializeMonacoEditor(codeOutline, language);

          });
        }
      });

      $('.programiz-challenge__editor--submit').click(function (e) {
        e.preventDefault();
        var code = monaco.editor.getModels()[0].getValue();

        var url_path = 'https://app.programiz.pro/community-challenges/preview/' + encodeURIComponent(slug) + '/info';

        var url_parameters =
          'code=' + encodeURIComponent(code) +
          '&title=' + encodeURIComponent(title) +
          '&id=' + encodeURIComponent(id);

        var utm =
          "utm_source=" + "article-programiz-web" +
          "&utm_medium=" + "article" +
          "&utm_campaign=" + "interactive-challenge_article-programiz-web";

        window.location.href = url_path + '?' + url_parameters + '&' + utm;
      });
    }
  }

  function initializeMonacoEditor(codeOutline, language) {
    var editor = monaco.editor.create(document.getElementById('programiz-challenge__editor--form'), {
      value: codeOutline,
      language: language,
      theme: 'vs-dark',
      lineNumbers: 'on',
      roundedSelection: false,
      scrollBeyondLastLine: false,
      readOnly: false,
      minimap: {
        enabled: false
      },
      fontSize: 14,
      quickSuggestions: false,
      parameterHints: false,
      hover: false,
      snippets: false,
      scrollbar: {
        alwaysConsumeMouseWheel: false
      }
    });
    
  }
})(jQuery, Drupal);

;/*})'"*/
;/*})'"*/
(function($){Drupal.behaviors.programiz_rate_share={attach:function(context,settings){$(".vote-up").click(function(){var nodeId=jQuery(this).parent().attr("data-nid");var cookieStatus;cookieStatus=setUpdateLikedDislikedCookie(nodeId,"liked");if(cookieStatus==="new"){handleLike(nodeId);}else if(cookieStatus==="updated"){updateToLike(nodeId);}
else{showLikeClickFeedback();}});$(".vote-down").click(function(){var nodeId=jQuery(this).parent().attr("data-nid");var cookieStatus;cookieStatus=setUpdateLikedDislikedCookie(nodeId,"disliked");if(cookieStatus==="new"){handleDislike(nodeId);}else if(cookieStatus==="updated"){updateToDisLike(nodeId);}
else{showDislikeClickFeedback();}});},};function setUpdateLikedDislikedCookie(nodeId,status){var cookieStatus="new";var cookieName="LikedDislikedArticle";var localStore=localStorage.getItem(cookieName);if(!localStore){localStorage.setItem(cookieName,JSON.stringify([]));}
var storeItems=JSON.parse(localStore)||[];var exisitingNode=storeItems.find(function(item){return item.nid==nodeId;});if(!exisitingNode){storeItems.push({nid:nodeId,visitedTime:new Date().getTime(),status:status,});}else{var currentStatus=storeItems.find(function(item){return item.nid==nodeId&&item.status==status;});cookieStatus="not changed";if(!currentStatus){exisitingNode.status=status;cookieStatus="updated";}}
localStorage.setItem(cookieName,JSON.stringify(storeItems));return cookieStatus;}
function handleLike(nodeId){jQuery.ajax({type:"GET",url:"/programiz_rate_share/liked",data:"nodeId="+nodeId,success:function(msg){},});showLikeClickFeedback();}
function handleDislike(nodeId){jQuery.ajax({type:"GET",url:"/programiz_rate_share/disliked",data:"nodeId="+nodeId,success:function(msg){},});showDislikeClickFeedback();}
function updateToDisLike(nodeId){jQuery.ajax({type:"GET",url:"/programiz_rate_share/update_to_dislike",data:"nodeId="+nodeId,success:function(msg){},});showDislikeClickFeedback();}
function updateToLike(nodeId){jQuery.ajax({type:"GET",url:"/programiz_rate_share/update_to_like",data:"nodeId="+nodeId,success:function(msg){},});showLikeClickFeedback();}
function showLikeClickFeedback(){loadLoadingGif();setTimeout(function(){jQuery(".loading-wrapper").remove();jQuery(".vote-wrapper").hide();jQuery(".share-wrapper").hide();jQuery(".vote-share-wrapper").addClass("like-feedback-container");var likeFeedbackText=getLikeFeedbackText();jQuery(".vote-share-wrapper").append(likeFeedbackText);},600);}
function showDislikeClickFeedback(){loadLoadingGif();setTimeout(function(){jQuery(".loading-wrapper").remove();jQuery(".vote-wrapper").hide();jQuery(".share-wrapper").hide();jQuery(".page-feedback-form").show();},600);}
function loadLoadingGif(){jQuery(".vote-up").hide();jQuery(".vote-down").hide();var loadingGif='<div class="loading-wrapper"><div id="loading" class="loading-reference">';jQuery(".vote-container").css({height:"60px",background:"#EAECF6",border:"2px solid #6501E5",});jQuery(".vote-container").append(loadingGif);}
function getLikeFeedbackText(){var text="";var fullUrl=window.location.href;var pageTitle=jQuery(document).find("title").text();text+="<div class='like-feedback-text'>We are glad you liked the article. Share with your friends.</div>";var facebookHref="https://www.facebook.com/sharer/sharer.php?u="+fullUrl;var twitterHref="https://twitter.com/intent/tweet?"+"text=Check this amazing article: "+
pageTitle+"&"+"via=programiz&"+"url="+
fullUrl;var whatsappHref="https://api.whatsapp.com//send?text=Check+this+amazing+article+on+"+
pageTitle+":+"+
fullUrl;var linkedinHref="https://www.linkedin.com/sharing/share-offsite/?url="+fullUrl;var facebookSvg='<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" > <circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333" /> <path fill-rule="evenodd" clip-rule="evenodd" d="M18.9167 10.168H17.1667C15.5558 10.168 14.25 11.4738 14.25 13.0846V14.8346H12.5V17.168H14.25V21.8346H16.5833V17.168H18.3333L18.9167 14.8346H16.5833V13.0846C16.5833 12.7625 16.8445 12.5013 17.1667 12.5013H18.9167V10.168Z" stroke="#0556F3" stroke-width="1.16999" stroke-linecap="round" stroke-linejoin="round" /> </svg>';var twitterSvg='<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" > <circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333" /> <path fill-rule="evenodd" clip-rule="evenodd" d="M22.4167 10.7521C21.8581 11.1461 21.2396 11.4475 20.585 11.6446C19.8654 10.8171 18.7058 10.527 17.6813 10.918C16.6568 11.309 15.9853 12.2981 16 13.3946V13.9779C13.9179 14.0319 11.9471 13.0399 10.75 11.3354C10.75 11.3354 8.41671 16.5854 13.6667 18.9187C12.4653 19.7342 11.0342 20.1431 9.58337 20.0854C14.8334 23.0021 21.25 20.0854 21.25 13.3771C21.2495 13.2146 21.2339 13.0525 21.2034 12.8929C21.7987 12.3058 22.2189 11.5645 22.4167 10.7521Z" stroke="#0556F3" stroke-width="1.22222" stroke-linecap="round" stroke-linejoin="round" /> </svg>';var whatsappSvg='<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" > <circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333" /> <path d="M21.0115 10.9885C19.7291 9.70613 18.0245 9 16.2108 9C16.2107 9 16.2103 9 16.2102 9C15.3132 9.00011 14.4391 9.17378 13.6122 9.51633C12.7853 9.85887 12.0445 10.3542 11.4101 10.9885C10.1278 12.2708 9.42169 13.9757 9.42169 15.7892C9.42169 16.8706 9.68263 17.9454 10.1771 18.9029L9.03589 22.163C8.95546 22.393 9.01239 22.6429 9.18479 22.8152C9.30538 22.9359 9.4641 23 9.62731 23C9.69727 23 9.76798 22.9883 9.83698 22.9641L13.0971 21.823C14.0546 22.3175 15.1294 22.5784 16.2108 22.5784C18.0243 22.5784 19.7291 21.8722 21.0115 20.5899C22.2938 19.3076 23 17.6027 23 15.7893C23 13.9757 22.2939 12.2708 21.0115 10.9885ZM20.4309 20.0093C19.3037 21.1366 17.8049 21.7572 16.2108 21.7572C15.2357 21.7572 14.2669 21.5161 13.4092 21.0596C13.2537 20.9769 13.0698 20.9627 12.9048 21.0205L9.94293 22.0571L10.9796 19.0952C11.0374 18.9299 11.0231 18.7461 10.9404 18.5907C10.484 17.7332 10.2428 16.7645 10.2428 15.7892C10.2428 14.1951 10.8635 12.6963 11.9907 11.5691C13.1178 10.4421 14.6164 9.82127 16.2103 9.82106H16.2108C17.805 9.82106 19.3037 10.4418 20.4309 11.5691C21.5582 12.6963 22.1789 14.195 22.1789 15.7892C22.1789 17.3833 21.5582 18.8821 20.4309 20.0093Z" fill="#0556F3" stroke="#0556F3" stroke-width="0.3" /> <path d="M18.734 16.3976C18.4216 16.0853 17.9134 16.0853 17.6011 16.3976L17.2595 16.7392C16.4113 16.277 15.725 15.5906 15.2627 14.7424L15.6043 14.4009C15.9167 14.0885 15.9167 13.5803 15.6043 13.268L14.6838 12.3475C14.3715 12.0352 13.8633 12.0352 13.5509 12.3475L12.8146 13.0839C12.3928 13.5057 12.3717 14.2308 12.7553 15.1258C13.0883 15.9028 13.6978 16.7569 14.4714 17.5305C15.2451 18.3042 16.0991 18.9137 16.8762 19.2467C17.3014 19.4289 17.6882 19.5198 18.0224 19.5198C18.3916 19.5198 18.6967 19.4088 18.9181 19.1874L19.6545 18.4509V18.451C19.8058 18.2997 19.8891 18.0986 19.8891 17.8846C19.8891 17.6706 19.8058 17.4695 19.6545 17.3182L18.734 16.3976ZM18.3375 18.6068C18.2171 18.7272 17.8469 18.7693 17.1997 18.4921C16.5163 18.1992 15.7536 17.6515 15.0521 16.9499C14.3505 16.2484 13.8029 15.4857 13.51 14.8024C13.2326 14.1552 13.2748 13.7849 13.3952 13.6645L14.1175 12.9422L15.0096 13.8344L14.582 14.2621C14.3887 14.4554 14.342 14.7486 14.466 14.9917C15.0281 16.094 15.9079 16.9738 17.0102 17.536C17.2535 17.66 17.5466 17.6134 17.74 17.42L18.1675 16.9924L19.0597 17.8846L18.3375 18.6068Z" fill="#0556F3" stroke="#0556F3" stroke-width="0.3" /> </svg>';var linkedinsvg='<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" > <circle cx="16" cy="16" r="15.3333" fill="white" stroke="#0556F3" stroke-width="1.33333" /> <path d="M13.3748 14.5417V20.375C13.3748 20.4524 13.3441 20.5265 13.2894 20.5812C13.2347 20.6359 13.1605 20.6667 13.0832 20.6667H11.6248C11.5475 20.6667 11.4733 20.6359 11.4186 20.5812C11.3639 20.5265 11.3332 20.4524 11.3332 20.375V14.5417C11.3332 14.4643 11.3639 14.3901 11.4186 14.3354C11.4733 14.2807 11.5475 14.25 11.6248 14.25H13.0832C13.1605 14.25 13.2347 14.2807 13.2894 14.3354C13.3441 14.3901 13.3748 14.4643 13.3748 14.5417ZM21.2498 16.8225C21.2596 16.2095 21.0596 15.6115 20.683 15.1277C20.3063 14.644 19.7757 14.3034 19.179 14.1625C18.773 14.0751 18.352 14.0861 17.9511 14.1947C17.5502 14.3033 17.1812 14.5063 16.8748 14.7867V14.5417C16.8748 14.4643 16.8441 14.3901 16.7894 14.3354C16.7347 14.2807 16.6605 14.25 16.5832 14.25H15.1248C15.0475 14.25 14.9733 14.2807 14.9186 14.3354C14.8639 14.3901 14.8332 14.4643 14.8332 14.5417V20.375C14.8332 20.4524 14.8639 20.5265 14.9186 20.5812C14.9733 20.6359 15.0475 20.6667 15.1248 20.6667H16.5832C16.6605 20.6667 16.7347 20.6359 16.7894 20.5812C16.8441 20.5265 16.8748 20.4524 16.8748 20.375V17.085C16.8679 16.8012 16.9611 16.524 17.1382 16.3021C17.3153 16.0802 17.5649 15.9278 17.8432 15.8717C18.0121 15.8425 18.1854 15.8509 18.3507 15.8964C18.516 15.9418 18.6693 16.0231 18.7996 16.1345C18.93 16.2459 19.0341 16.3846 19.1047 16.5408C19.1754 16.697 19.2107 16.8669 19.2082 17.0383V20.375C19.2082 20.4524 19.2389 20.5265 19.2936 20.5812C19.3483 20.6359 19.4225 20.6667 19.4998 20.6667H20.9582C21.0355 20.6667 21.1097 20.6359 21.1644 20.5812C21.2191 20.5265 21.2498 20.4524 21.2498 20.375V16.8225ZM12.2082 10.75C11.9774 10.75 11.7519 10.8184 11.56 10.9466C11.3681 11.0748 11.2186 11.257 11.1303 11.4702C11.042 11.6834 11.0189 11.918 11.0639 12.1443C11.1089 12.3706 11.2201 12.5785 11.3832 12.7416C11.5464 12.9048 11.7543 13.0159 11.9806 13.0609C12.2069 13.1059 12.4415 13.0828 12.6546 12.9945C12.8678 12.9062 13.05 12.7567 13.1782 12.5648C13.3064 12.373 13.3748 12.1474 13.3748 11.9167C13.3748 11.6072 13.2519 11.3105 13.0331 11.0917C12.8143 10.8729 12.5176 10.75 12.2082 10.75Z" fill="#0556F3" /> </svg>';var facebookLink='<div class="social-button-individual"><a class="social-icon__link" href="'+
facebookHref+'">';facebookLink+=facebookSvg;facebookLink+="</a></div>";var twitterLink='<div class="social-button-individual"><a class="social-icon__link" href="'+
twitterHref+'">';twitterLink+=twitterSvg;twitterLink+="</a></div>";var whatsappLink='<div class="social-button-individual"><a class="social-icon__link" href="'+
whatsappHref+'">';whatsappLink+=whatsappSvg;whatsappLink+="</a></div>";var linkedinLink='<div class="social-button-individual"><a class="social-icon__link" href="'+
linkedinHref+'">';linkedinLink+=linkedinsvg;linkedinLink+="</a></div>";var socialMediaLinks="<div class='share-buttons-container like-feedback-button'>"+
facebookLink+
twitterLink+
whatsappLink+
linkedinLink+"</div>";return text+socialMediaLinks;}})(jQuery);;;/*})'"*/
