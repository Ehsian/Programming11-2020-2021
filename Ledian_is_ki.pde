import java.util.Random;

int hilllocation = 0;
int hill2location = 0;
int cloud1location = 0;
int cloud2location = 300;
float cloud3location = 700;
int sunxpos = -50;
float sunypos = 100;
int carpos = 400;
boolean day = true;
void setup(){
  size(800,600);
  strokeWeight(0);
}

void draw(){
  if(day==true){
    background(3,173,255);
  }
  if(day==false){
    background(27,91,124);
  }
  
  if(day==true){fill(227,255,18);}
  else if(day==false){fill(255);}
  ellipse(sunxpos,sunypos,100,100);
  sunxpos+=1;
  if(sunxpos>400){sunypos+=0.25f;}
  else{sunypos-=0.25f;}
  if(sunxpos>=850){
    if(day==true){day=false;}
    else if(day==false){day=true;}
    sunxpos=-50;
  }
  
  stroke(3,255,93);
  fill(3,255,93);
  ellipse(hilllocation-400,400,400,400);
  ellipse(hilllocation,400,400,400);
  ellipse(hilllocation+400,400,400,400);
  ellipse(hilllocation+800,400,400,400);
  hilllocation +=2;
  if(hilllocation >=400){
    hilllocation = 0;
  }
  
  fill(17,118,45);
  ellipse(hill2location-200,400,200,200);
  ellipse(hill2location,400,200,200);
  ellipse(hill2location+200,400,200,200);
  ellipse(hill2location+400,400,200,200);
  ellipse(hill2location+600,400,200,200);
  ellipse(hill2location+800,400,200,200);
  hill2location+=4;
  if(hill2location >=200){
    hill2location = 0;
  }
  
  if(day==true){fill(255);}
  else if(day==false){fill(124);}
  ellipse(cloud1location,50,100,40);
  ellipse(cloud2location,130,150,60);
  ellipse(cloud3location,70,120,80);
  cloud1location +=1;
  cloud2location +=3;
  cloud3location +=1.5f;
  if (cloud1location >=1000){cloud1location = -100;}
  if (cloud2location >=1200){cloud2location = -100;}
  if (cloud3location >=900){cloud3location = -150;}
  
  fill(155);
  rect(0,400,800,200);
  
  
  if(day==false){
    stroke(255,255,0);
    fill(255,255,0,128);
    triangle(carpos-400,450,carpos-150,450,carpos,380);    
  }
  stroke(3,42,255);
  fill(3,42,255);
  rect(carpos-50,370,250,100);
  rect(carpos,300,150,70);
  fill(0);
  ellipse(carpos,450,70,70);
  ellipse(carpos+150,450,70,70);
  if(day==true){fill(255);}
  else if(day==false){fill(255,255,0);}
  ellipse(carpos-50,400,20,50);
  carpos-=1;
  if(carpos <= -200){carpos = 1000;}
  
  stroke(0,0,0,0);
}
