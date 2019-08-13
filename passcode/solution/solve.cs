using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace KosenCTF
{
    class Program
    {
        static List<int> correct_state;
        static List<int> vars;
        static List<int> indices;
        static List<int> state;


        static void shuffle()
        {
            int seed = 0;
            foreach (int x in state)
            {
                seed = seed * 10 + x;
            }
            Random rng = new Random(seed);
            for (int i = 0; i < 9; i++)
            {
                int j = rng.Next(9);
                int tmp = vars[i];
                vars[i] = vars[j];
                vars[j] = tmp;
            }
        }


        static void Main(string[] args)
        {
            correct_state = (from c in "231947329526721682516992571486892842339532472728294975864291475665969671246186815549145112147349184871155162521147273481838" select (int)(c - '0')).ToList();
            vars = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            indices = new List<int>();
            state = new List<int>();

            foreach (var x in correct_state) {
                var index = vars.IndexOf(x);
                indices.Add(index);
                state.Add(vars[index]);
                shuffle();
            }

            string flag = "";
            for (int i = 0; i < indices.Count / 3; i++)
            {
                flag += (char)(indices[i * 3] * 64 + indices[i * 3 + 1] * 8 + indices[i * 3 + 2]);
            }
            Console.WriteLine(flag);
        }
    }
}
