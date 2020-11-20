#include<fstream>
#include<cmath>

struct Error_Point
{
    double V;
    double e_V;
    double I;
    double e_I;

    Error_Point(){}
    friend std::istream& operator>>(std::istream& is, Error_Point& p)
    {
        is>>p.V>>p.e_V>>p.I>>p.e_I;
	return is;
    }
};

struct Error_Point_Array
{
    Error_Point el[10];
    Error_Point_Array(){}
    friend std::istream& operator>>(std::istream& is, Error_Point_Array& arr)
    {
        for(int i=0;i<10;i++)
	{
	    is>>arr.el[i];
	}
	return is;
    }
    friend std::ostream& operator<<(std::ostream& os, Error_Point_Array& arr)
    {
        os<<"V = [";
	for(int i=0;i<10;i++)
	{
	    os<<arr.el[i].V;
	    if( i < 9)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"e_V = [";
	for(int i=0;i<10;i++)
	{
	    os<<arr.el[i].e_V;
	    if( i < 9)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"I = [";
	for(int i=0;i<10;i++)
	{
	    os<<arr.el[i].I;
	    if( i < 9)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";

        os<<"e_I = [";
	for(int i=0;i<10;i++)
	{
	    os<<arr.el[i].e_I;
	    if( i < 9)
	        os<<", ";
	    else
	        os<<"]";
	}
	os<<"\n";
    }
};



int main() 
{
   std::ifstream input;
   input.open("calibrazione.txt");
   Error_Point_Array pydata;
   input>>pydata;
   input.close();

   std::ofstream output;
   output.open("calibrazione.py");
   output<<pydata;
   output.close();
   
   std::ifstream input_1;
   input_1.open("germanio.txt");
   Error_Point_Array pydata_1;
   input_1>>pydata_1;
   input_1.close();

   std::ofstream output_1;
   output_1.open("germanio.py");
   output_1<<pydata_1;
   output_1.close();
   
   std::ifstream input_2;
   input_2.open("silicio.txt");
   Error_Point_Array pydata_2;
   input_2>>pydata_2;
   input_2.close();

   std::ofstream output_2;
   output_2.open("silicio.py");
   output_2<<pydata_2;
   output_2.close();
}
