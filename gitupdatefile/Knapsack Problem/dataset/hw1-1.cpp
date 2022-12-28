#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
int main(){
    clock_t start,end;
    start=clock();
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
    int choose[a]={0},b[a]={0};
    int tw,tm,max=0;
    for(int i=0;i<pow(2,a);i++){
        tw=0;tm=0;
        for(int j=0;j<a;j++){
            if(choose[j]==1){
                tw+=weight[j];
                tm+=price[j];
            }              
        }            
        if(tm>max && tw<=cap){
            max=tm;
            for(int k=0;k<a;k++)
                b[k]=choose[k];
        }
            
        int o=0;
        choose[0]=!choose[0];
        o=!choose[0];
        for(int i=1;i<a;i++){
        choose[i]+=o;
        if(choose[i]>1){
            o=1;
            choose[i]=0;
        }
        else
            o=0;
        }
        end=clock();
        if(end-start>60000)
            break;
    }
    ofstream output("ans_"+folder+".txt");
    output<<max<<endl;
    for(int k=0;k<a;k++)
        output<<b[k]<<endl;
    cout<<max<<endl;
    output.close();
    return 0;
}