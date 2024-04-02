using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EpicSceneSwitcher : MonoBehaviour
{
    public string TargetScene;
    public Animator transitionAnimator;

    public GameManager manager;

    private void Awake()
    {
        manager = GameObject.FindGameObjectWithTag("GameManager").GetComponent<GameManager>();
        if (transitionAnimator != null)
        {
            transitionAnimator.SetBool("FirstTime", manager.firstTime);
        }
    }
    public void transitionStarter()
    {
        transitionAnimator.SetBool("SceneTransition", true);
        manager.firstTime = false;
    }
    public void SceneSwitcher()
    {
        SceneManager.LoadScene(TargetScene);
        
    }
    public void ApplicationCloser()
    {
        Application.Quit();
    }
}
