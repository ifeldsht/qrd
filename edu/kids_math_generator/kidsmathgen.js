function rand_int(min,max) {
  return Math.floor((max-min)*Math.random()+min);
}

function rand_half() {
  return Math.random() > 0.5;
}

function math_string(P) {
  if( P["name"] == "eq1" )       
    return gen_eq1(P["min"],P["max"]);
  if( P["name"] == "eq2" )       
    return gen_eq2(P["min"],P["max"]);
  if( P["name"] == "mul2big" )   
    return gen_mul2big(P["min"],P["max"]);
  if( P["name"] == "muladd" )    
    return gen_muladd(P["min"],P["max"],P["maxadd"]);
  if( P["name"] == "muladdmul" ) 
    return gen_muladdmul(P["min"],P["max"],P["maxadd"]);
  if( P["name"] == "muldiv" )    
    return gen_muldiv(P["min"],P["max"]);
  if( P["name"] == "mulcommon" ) 
    return gen_mulcommon();
  if( P["name"] == "addsub" )    
    return gen_addsub(P["min"],P["max"]);
  return "Unknown problem name";
}

function kids_math_generator(P) {
  str_out = "<table style=\"width:100%\">";
  for(i=0;i<P["rows"];i++) {
    str_out += "<tr>";
    for(j=0;j<P["cols"];j++) {
      str_out += "<td>" + math_string(P) + "</td>";
    }
    str_out += "</tr>";
  }
  str_out += "</table>";
  document.writeln(str_out);
}


/**************************************/

function gen_eq1(min,max) {
  a = rand_int(min,max);
  b = rand_int(min,max);
  return (a+b).toString() + " - .. = " + a.toString();
}

function gen_eq2(min,max) {
  a = rand_int(min,max);
  b = rand_int(min,max);
  return " .. - " + a.toString() + " = " + b.toString();
}

function gen_mul2big(max,min) {
  x1 = rand_int(min,max);
  x2 = rand_int(min,max);
  x3 = rand_int(min,max);
  x4 = rand_int(min,max);
  x5 = rand_int(min,max);
  a = 100 * x1 + 10 * x2 + x3;
  b = 10 * x4 + x5;
  r = " * ";
  return a.toString() + " * " + b.toString() + " = ..";
}

function gen_muladdmul(max,min,maxadd) {
  a = rand_int(min,max);
  b = rand_int(min,max);
  m = rand_int(min,max);
  r = " + ";
  c = rand_int(1,maxadd+1);
  if(rand_half()) {
    r = " - ";
    c = rand_int(0,a*b);
  }
  in_br = a.toString() + "*" + b.toString() + r + c.toString();
  return m.toString() + " * ( " + in_br + " ) = ..";
}

function gen_muladd(max,min,maxadd) {
  a = rand_int(min,max);
  b = rand_int(min,max);
  r = " + ";
  c = rand_int(1,maxadd+1);
  if(rand_half()) {
    r = " - ";
    c = rand_int(0,a*b);
  }
  return a.toString() + "*" + b.toString() + r + c.toString() + " = ..";
}

function gen_muldiv(max,min) {
  a = rand_int(min,max);
  b = rand_int(min,max);
  r = " * ";
  if(rand_half()) {
    r = " / ";
    a = a * b;
  }
  return a.toString() + r + b.toString() + " = ..";
}

function gen_mulcommon() {
  c = rand_int(1,10);
  if( rand_half() ) {
    a = rand_int(1,50);
    b = rand_int(5,10)*10;
    b = b - a;
    return c.toString() + "*" + a.toString() + " + " +
           c.toString() + "*" + b.toString() + " = ..";
  }
  a = rand_int(1,100);
  b = rand_int(1,a/10)*10 + a%10;
  return c.toString() + "*" + a.toString() + " - " +
         c.toString() + "*" + b.toString() + " = ..";
}

function gen_addsub(max,min) {
    a = rand_int(min,max);
    b = rand_int(min,max);
    r = " + ";
    if( rand_half() ) {
      r = " - ";
      if( b > a ) { x = b;  b = a; a = x; }
    }
    return a.toString() + r + b.toString() + " = ..";
}

/**************************************/

var P = {};
var query = window.location.search.substring(1);
var vars = query.split("&");
for(var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
    if( pair[0] != "name" ) P[pair[0]] = +pair[1];
    else P[pair[0]] = pair[1];
}

kids_math_generator(P);
