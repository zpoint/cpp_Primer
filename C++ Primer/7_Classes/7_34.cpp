#include <iostream>
#include <string>

class Screen {
		public:
				typedef std::string::size_type pos;
				void dummy_fcn(pos height)
				{
						cursor = width * height;
				}
		private:
				pos cursor = 0;
				pos height = 0, width = 0;
};

int main()
{
		/*
		 * If move line 6 to the end of class, program will not compile
		 */
		Screen s;
		return 0;
}
