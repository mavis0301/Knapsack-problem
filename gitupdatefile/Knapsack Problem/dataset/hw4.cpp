#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<random>
#include<ctime>
#include<vector>
using namespace std;
int main(){
    srand(time(NULL));
    string folder;
    cout<<"type your folder(ds1/ds2/ds3/ds4) : ";
    cin>>folder;
    
    ifstream c(folder+"/c.txt");
    if(!c){
        cout<<"file c.txt not found"<<endl;
    }
    int cap,weight[1000],price[1000],a=0;
    c>>cap;
    c.close();
    ifstream w(folder+"/w.txt"),p(folder+"/p.txt");
    while(w>>weight[a] && p>>price[a]){
        a++;
    }
    p.close();
    w.close();

    bool ch[a]={false};
    vector<int> one;
    vector<int>::iterator it;
    //vector<int> z;
    int r,sum,total;
    double T=100,TF=0.0000001,tc=0.99;
    int best=0,delta=0,r2;
    int bestCh[a]={0};
    for(int i=0;i<a;i++){
        bestCh[i]=1;
        one.push_back(i);
    }
    
    while(T>TF){
        for(int j=0;j<1000000;j++){
            for(int k=0;k<a/100+1;k++){
                r=rand()%a;
                if(ch[r]==0)
                    ch[r]=!ch[r];
                else{
                    k--;
                    continue;
                }
                one.push_back(r);
            }
            
            
 
            sum=0;
            for(int i=0;i<a;i++){       //重量總和
                sum+=ch[i]*weight[i];
            }
            while(sum>cap){
                int rr=rand()%one.size();
                int zero=one[rr];
                one.erase(one.begin()+rr);
                ch[zero]=0;
                sum=0;
                for(int i=0;i<a;i++){
                    sum+=ch[i]*weight[i];   //重量總和
                }
            }
            total=0;
            for(int i=0;i<a;i++)
                total+=ch[i]*price[i];  //價值總和
            delta=best-total;
            if(delta<0){
                best=total;
                for(int i=0;i<a;i++){
                    bestCh[i]=ch[i];
                }
            }
            else{
                int r1=(float)rand()/(float)RAND_MAX;
                if(r1<exp(-(float)delta/T)){
                    best=total;
                    for(int i=0;i<a;i++){
                        bestCh[i]=ch[i];
                    }
                }
            }
            T=T*tc;
        }
    }
    ofstream output("ans_"+folder+".txt");
    output<<best<<endl;
    for(int i=0;i<a;i++)
        output<<bestCh[i]<<endl;
    output.close();
    return 0;
}