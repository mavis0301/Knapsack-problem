#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cstring>
using namespace std;
int w[1000],p[1000];

int main()
{
	fstream Cfile,Wfile,Pfile,Outfile;
	string fileName,C,W,P;
	cout<<"Select the file name:"<<endl;
	cin>>fileName;
	C=fileName+"/c.txt";
	W=fileName+"/w.txt";
	P=fileName+"/p.txt";
	Cfile.open(C.c_str(),ios::in);
	Wfile.open(W.c_str(),ios::in);
	Pfile.open(P.c_str(),ios::in);

	int c,n=0;
	Cfile>>c;
	//int dp[c+1];
	int* dp= new int[c+1];
	for(int i=0;i<=c;i++){
        dp[i]=0;
    }
	int **comp=new int*[1000];
	for(int i=0;i<1000;i++)
		comp[i]=new int[c+1];
	int ans[1000];
	//memset(dp,0,sizeof(dp));
	memset(ans,false,sizeof(ans));
	for(int i=0;i<1000;i++)
		memset(comp[i],false,sizeof(comp[i]));
	while(!Wfile.eof())
	{
		Wfile>>w[n];
		if(Wfile.fail())
			break;
		Pfile>>p[n];
		n++;
	}
	//cout<<n<<endl;
	Cfile.close();
	Wfile.close();
	Pfile.close();
	for(int i=0;i<1000;i++)
	{
		for(int j=c;j>=0;j--)
		{
			if(j<w[i])
				break;
			if(dp[j]<dp[j-w[i]]+p[i])
			{
				dp[j]=dp[j-w[i]]+p[i];
				comp[i][j]=1;
			}
			
			
		}
	}
	fileName="ans_"+fileName+".txt";
	Outfile.open(fileName.c_str(),ios::out);
	Outfile<<dp[c]<<endl;
	cout<<dp[c]<<endl;
	int j=c;
	for(int i=n-1;i>=0;i--)
	{
		if(comp[i][j])
		{
			ans[i]=true;
			j=j-w[i];
		}
	}
	for(int i=0;i<n;i++)
		Outfile<<int(ans[i])<<endl;
	cout<<"Finish!"<<endl;
	Outfile.close();

	return 0;
}
