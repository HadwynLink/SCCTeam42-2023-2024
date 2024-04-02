using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace diseaseClassLib
{
    public class radWave
    {
        public string Name { get; set; }
        public List<string> SystemsHit { get; set; }

        public radWave(string radName, List<string> systemshit)
        {
            Name = radName;
            SystemsHit = systemshit;
        }
    }
    public class Injury
    {
        public string Name { get; set; }
        public int Severity { get; set; }
        public string currentSymptoms { get; set; }
        public List<string> allSymptoms { get; set; }

        public Injury(string injname, int severity, string currentsymps, List<string> allsymps)
        {
            Name = injname;
            Severity = severity;
            currentSymptoms = currentsymps;
            allSymptoms = allsymps;
        }
    }
    public class Cancer
    {
        public string Name { get; set; }
        public float Probability { get; set; }
        public string currentSymptoms { get; set; }
        public string Type { get; set; }

        public Cancer(string cancername, float probability, string currentsymps, string type)
        {
            Name = cancername;
            Probability = probability;
            currentSymptoms = currentsymps;
            Type = type;
        }
    }

}
