using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using diseaseClassLib;

public class classRepo : MonoBehaviour
{
    public radWave Photon = new radWave("Photon", new List<string>() { "Skin", "Bone", "Lung", "Brain", "Heart", "Reproductive", "Digestive" });
    public radWave Electron = new radWave("Electron", new List<string>() { "Skin" });
    public radWave Carbon = new radWave("Carbon", new List<string>() { "Skin", "Bone", "Lung", "Brain", "Heart", "Reproductive", "Digestive" });
    public radWave Neon = new radWave("Neon", new List<string>() { "Skin", "Bone", "Lung", "Brain", "Heart", "Reproductive", "Digestive" });
    public radWave Proton = new radWave("Proton", new List<string>() { "Skin", "Bone" });

    public Injury ARS = new Injury("Acute Radiation Syndrome", 0, "None", new List<string>()
        {"No noticeable symptoms",
        "Slight headaches, fatigue, weakness",
        "Cognitive impairment, Hemmorage infections, Leukopenia",
        "Extreme ulcers, sclerosis, nausea, diarrhea, high fever",
        "Shock, nausea, vomiting, incapacitation" });
    public Injury CRI = new Injury("Cutaneous Radiation Injury", 0, "None", new List<string>()
        {"No noticeable symptoms",
        "Mild skin atrophy",
        "Potential ulcers, moderate skin atrophy",
        "Extreme ulcers, sclerosis, nausea, etc.",
        "Complete skin necrosis"});
    public Injury Overall = new Injury("Overall Health", 0, "None", new List<string>()
        {"No cancer risk",
        "Small risk of developing cancer",
        "Mild risk of cancer",
        "Observable health effects. Moderately increased risk of cancer",
        "Nausea, vomiting, tremors. Significantly increased cancer risk.",
        "Worsening Acute Radiation Sickness. Permanent damage",
        "Loss of hair. 50% death expectancy within a month.",
        "Death expected within a week.",
        "Certain death within days"});

    public Cancer ALK = new Cancer("Lymphoma", 0, "swelling, fatigue, fever, shortness of breath, skin irritation, weight loss", "Heart");
    public Cancer BCL1 = new Cancer("Bladder Cancer", 0, "blood in urine, frequent/painful urination, back pain", "Digestive");
    public Cancer BCL2 = new Cancer("B-Cell Lymphoma", 0, "swelling, fatigue, fever, shortness of breath, skin irritation, weight loss", "Heart");
    public Cancer BCRABL = new Cancer("Myelogenous Leukemia", 0, "fever, fatigue and weakness, frequent infections, weight loss, swollen liver and spleen, easy bleeding, red spots on skin, night sweating, bone pain", "Heart");
    public Cancer CDK4 = new Cancer("Sarcoma", 0, "skin lumps, bone pain, fragile bones, abdominal pain, weight loss", "Bone");
    public Cancer EFGR = new Cancer("Breast Cancer", 0, "breast lumps, change in breast shape, skin dimples, inverted nipples, peeling/crusting around breast skin", "Reproductive");
    public Cancer MET = new Cancer("Gastric Tumors", 0, "trouble swallowing, belly pain, feeling bloated/unnaturally full, strange hunger cycle, heartburn, indigestion, black excrement", "Digestive");
    public Cancer MYB = new Cancer("Melanoma", 0, "unusual skin growth, large asymmetrical moles which change over time", "Skin");
    public Cancer RAF1 = new Cancer("Lung Cancer", 0, "persistent cough, coughing blood, shortness of breath, chest pain, loss of voice, bone pain, headache", "Lung");
    public Cancer REL = new Cancer("Non-Hodgkin Lymphoma", 0, "swollen lymph nodes in extremities, abdominal swelling, chest pain and trouble breathing, fatigue, fever, night sweats, weight loss", "Heart");
    public Cancer FOS = new Cancer("Osteosarcoma", 0, "swelling near bones, bone and joint pain, unexplainable bone injuries", "Bone");
    public Cancer cMYC = new Cancer("Colon Cancer", 0, "frequent diarrhea and constipation, rectal bleeding/bloody stool, persistent digestive issues, bowel not emptying completely, weakness, weight loss", "Digestive");
    public Cancer BRCA1 = new Cancer("Ovarian Cancer", 0, "abdominal bloating, getting full without much food, weight loss, pelvic discomfort, fatigue, back pain, constipation, frequent urination", "Reproductive");
    public List<Cancer> contractableCancers = new List<Cancer>();
    private void Awake()
    {
        contractableCancers.Add(ALK);
        contractableCancers.Add(BCL1);
        contractableCancers.Add(BCL2);
        contractableCancers.Add(BCRABL);
        contractableCancers.Add(CDK4);
        contractableCancers.Add(EFGR);
        contractableCancers.Add(MET);
        contractableCancers.Add(MYB);
        contractableCancers.Add(RAF1);
        contractableCancers.Add(REL);
        contractableCancers.Add(FOS);
        contractableCancers.Add(cMYC);
        contractableCancers.Add(BRCA1);
    }
}
