using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using System.IO;
using diseaseClassLib;

public class CancerRunner : MonoBehaviour
{
    public classRepo info;
    float time = 0;
    public float timeScale = 1;

    public GameManager manager;
    public TextMeshProUGUI greyOutput;
    public TextMeshProUGUI sievertOutput;
    public TextMeshProUGUI healthOutput;

    public TextMeshProUGUI ARS_output;
    public TextMeshProUGUI CRI_output;
    public TextMeshProUGUI CancersOutput;

    public TextMeshProUGUI timerOutput;
    public TextMeshProUGUI exposedRadiation1Output;
    public TextMeshProUGUI exposedRadiation2Output;
    public TextMeshProUGUI energyAbsorbedOutput;
    public TextMeshProUGUI unblockedEnergyOutput;
    public TextMeshProUGUI radiationBlockedOutput;
    public RectTransform sliderRect;

    public ParticleSystemRenderer RadIn;
    public ParticleSystemRenderer RadOut1;
    public ParticleSystemRenderer RadOut2;
    public ParticleSystem RadSetIn;
    public ParticleSystem RadOutSet1;
    public ParticleSystem RadOutSet2;
    public MaterialSwitcher materials;

    public string fileName = "";
    string directory;
    StreamReader sr;
    char[] charSeparators = new char[] {','};

    public string targetRadiation = "Gamma";
    public string targetWall = "Concrete";
    public string targetSpeed = "slow";

    List<string> savedListedValues = new List<string>();
    Dictionary<string, float> CurrentDosage = new Dictionary<string, float>();
    List<string> bodyParts = new List<string>() {"Skin", "Bone", "Lung", "Brain", "Heart", "Reproductive", "Digestive" };

    float subjectMass;
    float subjectSA;
    float dt;
    radWave radType1;
    float energyAmt1;
    radWave radType2;
    float energyAmt2;

    public float TotalGy = 0;
    public float TotalSv = 0;

    public bool noRad1 = false;
    public bool noRad2 = false;
    bool survivable = true;

    // Start is called before the first frame update
    void Start()
    {
        CurrentDosage.Add("Skin", 0);
        CurrentDosage.Add("Bone", 0);
        CurrentDosage.Add("Lung", 0);
        CurrentDosage.Add("Brain", 0);
        CurrentDosage.Add("Heart", 0);
        CurrentDosage.Add("Reproductive", 0);
        CurrentDosage.Add("Digestive", 0);

        manager = GameObject.FindGameObjectWithTag("GameManager").GetComponent<GameManager>();

        switch (manager.RadType)
        {
            case 0:
                targetRadiation = "Gamma";
                RadIn.material = materials.Gamma;
                RadIn.trailMaterial = materials.GammaTrail;
                break;
            case 1:
                targetRadiation = "Carbon";
                RadIn.material = materials.Carbon;
                RadIn.trailMaterial = materials.CarbonTrail;
                break;
            case 2:
                targetRadiation = "Neon";
                RadIn.material = materials.Neon;
                RadIn.trailMaterial = materials.NeonTrail;
                break;
            case 3:
                targetRadiation = "Proton";
                RadIn.material = materials.Proton;
                RadIn.trailMaterial = materials.ProtonTrail;
                break;
            default:
                break;
        }
        switch (manager.RadSpeed)
        {
            case 0:
                targetSpeed = "fast";
                break;
            case 1:
                targetSpeed = "slow";
                break;
            default:
                break;
        }
        switch (manager.WallMat)
        {
            case 0:
                targetWall = "Water";
                break;
            case 1:
                targetWall = "Al";
                break;
            case 2:
                targetWall = "Concrete";
                break;
            case 3:
                targetWall = "Pb";
                break;
            case 4:
                targetWall = "Kapton";
                break;
            default:
                break;
        }
        string filepath = Application.streamingAssetsPath + "\\Data\\";
        directory = filepath + fileName;
        sr = new StreamReader(directory);
        string radTypeInput = "";
        string wallTypeInput = "";
        string speedTypeInput = "";
        int cutoffloops = 0;
        sr.ReadLine();
        while (!(radTypeInput == targetRadiation && wallTypeInput == targetWall && speedTypeInput == targetSpeed) || cutoffloops > 64)
        {
            List<string> listedValues = new List<string>();
            string currentLine = sr.ReadLine();
            string[] data_values = currentLine.Split(charSeparators, System.StringSplitOptions.RemoveEmptyEntries);
            foreach (var value in data_values)
            {
                listedValues.Add(value);
            }
            radTypeInput = listedValues[0];
            wallTypeInput = listedValues[1];
            speedTypeInput = listedValues[7];
            cutoffloops++;
            if ((radTypeInput == targetRadiation && wallTypeInput == targetWall && speedTypeInput == targetSpeed))
            {
                savedListedValues = listedValues;
            }
        }

        dt = float.Parse(savedListedValues[8]);
        timeScale = manager.simSpeed;

        switch (savedListedValues[9])
        {
            case "Proton":
                radType1 = info.Proton;
                RadOut1.material = materials.Proton;
                RadOut1.trailMaterial = materials.ProtonTrail;
                break;
            case "Photon":
                radType1 = info.Photon;
                RadOut1.material = materials.Photon;
                RadOut1.trailMaterial = materials.PhotonTrail;
                break;
            case "Neon":
                radType1 = info.Neon;
                RadOut1.material = materials.Neon;
                RadOut1.trailMaterial = materials.NeonTrail;
                break;
            case "Carbon":
                radType1 = info.Carbon;
                RadOut1.material = materials.Carbon;
                RadOut1.trailMaterial = materials.CarbonTrail;
                break;
            case "e-":
                radType1 = info.Electron;
                RadOut1.material = materials.Electron;
                RadOut1.trailMaterial = materials.ElectronTrail;
                break;
            default:
                noRad1 = true;
                RadOut1.enabled = false;
                break;
        }
        var Rad1emission = RadOutSet1.emission;
        Rad1emission.rateOverTime = Mathf.Max(5 * (float.Parse(savedListedValues[11]) / (float.Parse(savedListedValues[3]) + float.Parse(savedListedValues[2]))), 0.5f);
        switch (savedListedValues[12])
        {
            case "Proton":
                radType2 = info.Proton;
                RadOut2.material = materials.Proton;
                RadOut2.trailMaterial = materials.ProtonTrail;
                break;
            case "Photon":
                radType2 = info.Photon;
                RadOut2.material = materials.Photon;
                RadOut2.trailMaterial = materials.PhotonTrail;
                break;
            case "Neon":
                radType2 = info.Neon;
                RadOut2.material = materials.Neon;
                RadOut2.trailMaterial = materials.NeonTrail;
                break;
            case "Carbon":
                radType2 = info.Carbon;
                RadOut2.material = materials.Carbon;
                RadOut2.trailMaterial = materials.CarbonTrail;
                break;
            case "e-":
                radType2 = info.Electron;
                RadOut2.material = materials.Electron;
                RadOut2.trailMaterial = materials.ElectronTrail;
                break;
            default:
                noRad2 = true;
                RadOut2.enabled = false;
                break;
        }
        var Rad2emission = RadOutSet2.emission;
        Rad2emission.rateOverTime = Mathf.Max(5 * (float.Parse(savedListedValues[14]) / (float.Parse(savedListedValues[3]) + float.Parse(savedListedValues[2]))), 0.1f);
        if (noRad1 == false)
        {
            exposedRadiation1Output.text = "Unblocked Radiation Type 1: " + radType1.Name;
        }
        else
        {
            exposedRadiation1Output.text = "Unblocked Radiation Type 1: None";
        }
        if (noRad2 == false)
        {
            exposedRadiation2Output.text = "Unblocked Radiation Type 2: " + radType2.Name;
        }
        else
        {
            exposedRadiation2Output.text = "Unblocked Radiation Type 2: None";
        }

        energyAmt1 = float.Parse(savedListedValues[11]) * 1000f;
        energyAmt2 = float.Parse(savedListedValues[14]) * 1000f;
        subjectMass = manager.subjectMass;
        subjectSA = manager.subjectSA;

        greyOutput.text = "all your greyse are belong to us";
        sievertOutput.text = "all your sievertse are belong to us";
        healthOutput.text = "all your healthse are belong to us";
        ARS_output.text = "all your ARSse are belong to us";
        CRI_output.text = "all your CRIse are belong to us";
        CancersOutput.text = info.REL.Name + ": " + info.REL.Type + " cancer, " + info.REL.Probability + "% chance \n" + "     Symptoms: " + info.REL.currentSymptoms;
    }

    // Update is called once per frame
    void Update()
    {
        if (survivable)
        {
            float Gy1 = graycalc(energyAmt1, subjectMass, subjectSA) * timeScale;
            float Gy2 = graycalc(energyAmt2, subjectMass, subjectSA) * timeScale;
            float NewGy = Gy1 + Gy2;
            float Sv1 = 0;
            if (!noRad1)
            {
                Sv1 = sievertcalc(Gy1, radType1.Name);
            }
            float Sv2 = 0;
            if (!noRad2)
            {
                Sv2 = sievertcalc(Gy2, radType2.Name);
            }
            float NewSv = Sv1 + Sv2;
            TotalGy += NewGy;
            TotalSv += NewSv;

            foreach (string bodypart in bodyParts)
            {
                if (!noRad1)
                {
                    if (radType1.SystemsHit.Contains(bodypart))
                    {
                        CurrentDosage[bodypart] += effDoseCalc(Sv1, bodypart);
                        print(bodypart + ": " + CurrentDosage[bodypart]);
                    }
                }
                if (!noRad2)
                {
                    if (radType2.SystemsHit.Contains(bodypart))
                    {
                        CurrentDosage[bodypart] += effDoseCalc(Sv2, bodypart);
                    }
                }
                foreach (Cancer disease in info.contractableCancers)
                {
                    if (disease.Type == bodypart)
                    {
                        disease.Probability = Mathf.Min(CurrentDosage[bodypart] * 5.5f, 100);
                    }
                }
            }

            if (TotalGy < 2)
            {
                info.ARS.Severity = 0;
                info.ARS.currentSymptoms = info.ARS.allSymptoms[info.ARS.Severity];
                info.CRI.Severity = 0;
                info.CRI.currentSymptoms = info.CRI.allSymptoms[info.CRI.Severity];
            }
            else if (TotalGy < 6)
            {
                info.ARS.Severity = 1;
                info.ARS.currentSymptoms = info.ARS.allSymptoms[info.ARS.Severity];
            }
            else if (TotalGy < 8)
            {
                info.ARS.Severity = 2;
                info.ARS.currentSymptoms = info.ARS.allSymptoms[info.ARS.Severity];
                info.CRI.Severity = 1;
                info.CRI.currentSymptoms = info.CRI.allSymptoms[info.CRI.Severity];
            }
            else if (TotalGy < 15)
            {
                info.CRI.Severity = 2;
                info.CRI.currentSymptoms = info.CRI.allSymptoms[info.CRI.Severity];
            }
            else if (TotalGy < 30)
            {
                info.ARS.Severity = 3;
                info.ARS.currentSymptoms = info.ARS.allSymptoms[info.ARS.Severity];
                info.CRI.Severity = 3;
                info.CRI.currentSymptoms = info.CRI.allSymptoms[info.CRI.Severity];
            }
            else if (TotalGy > 30)
            {
                info.ARS.Severity = 4;
                info.ARS.currentSymptoms = info.ARS.allSymptoms[info.ARS.Severity];
                info.CRI.Severity = 4;
                info.CRI.currentSymptoms = info.CRI.allSymptoms[info.CRI.Severity];
            }

            if (TotalSv < 50 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 0;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 100 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 1;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 500 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 2;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 1000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 3;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 2000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 4;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 3000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 5;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 5000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 6;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 10000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 7;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }
            else if (TotalSv < 50000 * Mathf.Pow(10, -3))
            {
                info.Overall.Severity = 8;
                info.Overall.currentSymptoms = info.Overall.allSymptoms[info.Overall.Severity];
            }

            if (TotalGy > 30 || TotalSv > 50)
            {
                survivable = false;
                timerOutput.text = "Subject is dead. Time Elapsed: " + time + " seconds.";
            }
            else
            {
                time += dt * timeScale;
                timerOutput.text = "Time Elapsed: " + time + " seconds";
            }

            greyOutput.text = "Total Grays Absorbed: " + decimal.Round((decimal)TotalGy, 3) + " Gy";
            sievertOutput.text = "Total Sieverts Absorbed: " + decimal.Round((decimal)TotalSv, 3) + " Sv";
            healthOutput.text = "Overall Health: \n" + info.Overall.currentSymptoms;
            ARS_output.text = info.ARS.Name + ": \n" + info.ARS.currentSymptoms;
            CRI_output.text = info.CRI.Name + ": \n" + info.CRI.currentSymptoms;
            CancersOutput.text = "";
            int cancerWindowExpansion = 0;
            foreach (Cancer disease in info.contractableCancers)
            {
                if (disease.Probability >= .1)
                {
                    CancersOutput.text += disease.Name + ": " + disease.Type + " cancer, " + decimal.Round((decimal)disease.Probability, 1) + "% chance \n" + "     Symptoms: " + disease.currentSymptoms + "\n\n";
                    cancerWindowExpansion++;
                }
            }
            sliderRect.sizeDelta = new Vector2(sliderRect.sizeDelta.x, 160.22f + (60 * cancerWindowExpansion));
            energyAbsorbedOutput.text = "Total Energy Absorbed: " + decimal.Round((decimal)(float.Parse(savedListedValues[2]) * time), 3) + "KeV";
            radiationBlockedOutput.text = "Radiation Blocked: " + decimal.Round((decimal)(float.Parse(savedListedValues[2]) / (float.Parse(savedListedValues[3]) + float.Parse(savedListedValues[2]))*100), 2) + "%";
            unblockedEnergyOutput.text = "Total Unblocked Energy: " + decimal.Round((decimal)(float.Parse(savedListedValues[3]) * time),3) + "KeV";
        }
    }

    public float graycalc(float eVm, float avgweight, float avgSA)
    {
        float joulem = (float)(eVm * 1.6028 * Mathf.Pow(10, -19));
        float greyNum = joulem * avgSA/ (2 * avgweight);
        return greyNum;
    }
    public float sievertcalc(float grays, string radType)
    {
        switch (radType)
        {
            case "Gamma":
                return grays * 1;
            case "Proton":
                return grays * 3;
            case "Photon":
                return grays * 1;
            case "Neon":
                return grays * 20;
            case "Carbon":
                return grays * 20;
            case "e-":
                return grays * 1;
            default:
                return grays * 1;
        }
    }
    public float effDoseCalc(float sieverts, string bodypart)
    {
        float effDose = 0f;
        switch (bodypart)
        {
            case "Skin":
                effDose = sieverts * 0.01f;
                return effDose;
            case "Bone":
                effDose = sieverts * 0.13f;
                return effDose;
            case "Lung":
                 effDose = sieverts * 0.21f;
                return effDose;
            case "Brain":
                 effDose = sieverts * 0.01f;
                return effDose;
            case "Heart":
                 effDose = sieverts * 0.12f;
                return effDose;
            case "Reproductive":
                 effDose = sieverts * 0.2f;
                return effDose;
            case "Digestive":
                 effDose = sieverts * 0.32f;
                return effDose;
            default:
                return 0;
        }
    }

}
