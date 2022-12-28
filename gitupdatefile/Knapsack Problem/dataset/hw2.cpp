#include<iostream>
#include<string>
#include<fstream>
#include<map>
using namespace std;
int main(){
    string folder;
    cout<<"type your folder(ds1/ds2/ds3) : ";
    cin>>folder;
    ifstream c(folder+"/c.txt");
    if(!c){
        cout<<"file c.txt not found"<<endl;
    }
    int cap,weight[50],price[50],a=0;
    c>>cap;
    c.close();
    ifstream w(folder+"/w.txt"),p(folder+"/p.txt");
    while(w>>weight[a] && p>>price[a]){
        a++;
    }
    p.close();
    w.close();
    map<double,int> l;
    double cp;
    for(int i=0;i<a;i++){
        cp=(float)price[i]/(float)weight[i];
        l[cp]=i;

    }
    int up[a],j=a-1;
    for(auto itr = l.begin(); itr != l.end(); ++itr){
		up[j]=itr->second;
        j--;
	}
    int final[a]={0},max=0;
    j=0;
    while(cap>0 && j<a){
        if(cap-weight[up[j]]>=0){
            cap-=weight[up[j]];
            final[up[j]]=1;
            max+=price[up[j]];
        }
        j++;
    }
    ofstream output("ans_"+folder+".txt");
    output<<max<<endl;
    for(int i=0;i<a;i++){
        output<<final[i]<<endl;
    }
    cout<<max<<endl;
    output.close();
}