#include<iostream>
using namespace std;

void wone(){
	bool err=true;
	bool err1=true;
	if (err){throw 10;}
	if (err1){throw "String error"};
}

int main(){

try{
wone();
}
catch(int e){
cout<<"Caught e: "<<e<<endl;
}
catch(char const * e){
cout<<"Caught e: "<<e<<endl;
}
return 0;
}
