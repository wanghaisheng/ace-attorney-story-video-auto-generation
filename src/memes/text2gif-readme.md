https://github.com/akzhy/Vara

利用js先将文案 背景图片 生成对应的gif
npm install vara --save




new Vara("#container","font.json",[
{
	text:"Hello World", // String, text to be shown
	fontSize:24, // Number, size of the text
	strokeWidth:.5, // Width / Thickness of the stroke
	color:"black", // Color of the text
	id:"", // String or integer, for if animations are called manually or when using the get() method. Default is the index of the object.
	duration:2000, // Number, Duration of the animation in milliseconds
	textAlign:"left", // String, text align, accepted values are left,center,right
	x:0, // Number, x coordinate of the text
	y:0, // Number, y coordinate of the text
	fromCurrentPosition:{ // Whether the x or y coordinate should be from its calculated position, ie the position if x or y coordinates were not applied
		x:true, // Boolean
		y:true, // Boolean
	},
	autoAnimation:true, // Boolean, Whether to animate the text automatically
	queued:true, // Boolean, Whether the animation should be in a queue
    delay:0,     // Delay before the animation starts in milliseconds
    /* Letter spacing can be a number or an object, if number, the spacing will be applied to every character.
    If object, each letter can be assigned a different spacing as follows,
    letterSpacing: {
        a: 4,
        j: -6,
        global: -1
    }
    The global property is used to set spacing of all other characters
    */
	letterSpacing:0
}],{
	// The options given below will be applicable to every text created,
	// however they will not override the options set above.
	// They will work as secondary options.
	fontSize:24, // Number, size of the text
	strokeWidth:.5, // Width / Thickness of the stroke
	color:"black", // Color of the text
	duration:2000, // Number, Duration of the animation in milliseconds
	textAlign:"left", // String, text align, accepted values are left,center,right
	autoAnimation:true, // Boolean, Whether to animate the text automatically
	queued:true, // Boolean, Whether the animation should be in a queue
	letterSpacing:0
})





var ctx = document.querySelector("canvas").getContext("2d"),
    dashLen = 220, dashOffset = dashLen, speed = 5,
    txt = "STROKE-ON CANVAS", x = 30, i = 0;

ctx.font = "50px Comic Sans MS, cursive, TSCu_Comic, sans-serif"; 
ctx.lineWidth = 5; ctx.lineJoin = "round"; ctx.globalAlpha = 2/3;
ctx.strokeStyle = ctx.fillStyle = "#1f2f90";

(function loop() {
  ctx.clearRect(x, 0, 60, 150);
  ctx.setLineDash([dashLen - dashOffset, dashOffset - speed]); // create a long dash mask
  dashOffset -= speed;                                         // reduce dash length
  ctx.strokeText(txt[i], x, 90);                               // stroke letter

  if (dashOffset > 0) requestAnimationFrame(loop);             // animate
  else {
    ctx.fillText(txt[i], x, 90);                               // fill final letter
    dashOffset = dashLen;                                      // prep next char
    x += ctx.measureText(txt[i++]).width + ctx.lineWidth * Math.random();
    ctx.setTransform(1, 0, 0, 1, 0, 3 * Math.random());        // random y-delta
    ctx.rotate(Math.random() * 0.005);                         // random rotation
    if (i < txt.length) requestAnimationFrame(loop);
  }
})();

canvas {background:url(http://i.imgur.com/5RIXWIE.png)}

<canvas width=630></canvas>




python的话 
https://github.com/cduck/drawSvg/issues/47
这种不知道行不行
https://github.com/cduck/drawSvg/issues/21



from PIL import Image, ImageDraw, ImageSequence
import io

im = Image.open('Tests/images/iss634.gif')

frames = []
for frame in ImageSequence.Iterator(im):
	frame = frame.convert('RGB')
	
	d = ImageDraw.Draw(frame)
	d.text((10,100), "Hello World", fill=(255,255,255))
	del d
	
	frames.append(frame)
my_bytes = io.BytesIO()
frames[0].save(my_bytes, format="GIF", save_all=True, append_images=frames[1:])
print(my_bytes.getvalue())