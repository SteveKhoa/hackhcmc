


<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SteveKhoa/hackhcmc">
    <h3 align="center">Heineken Scan</h3>
  </a>

  <p align="center">
    A tool is created by GoBigGoHome team in order to help Heineken company observe their products through images.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
 <table>
  <tr>
    <td><img src="https://github.com/SteveKhoa/hackhcmc/assets/113105084/198da34c-4ea0-429b-bc79-2cd6e9af9865" alt="Image 1 Description" width="500"/></td>
    <td><img src="https://github.com/SteveKhoa/hackhcmc/assets/113105084/394d64ec-aeb6-478e-8a70-698522e3d1ec" alt="Image 2 Description" width="500"/></td>
  </tr>
</table>
</div>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* ![Git][Git]
* [![VStudio][VStudio]][VStudio-url]
* [![GoogleColab][GoogleColab]][GoogleColab-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

*How to run the app ?*

### --> Using source code
1. Download source code 
2. Create python virtual environment ( for MacOS )
* cmd
  ```sh
    python3.10 -m venv. venv  
  ```
3. Install python dependencies ( Make sure virtual environment turn on )
* cmd
  ```sh
    pip install -r requirements.txt  
  ```
4. There are 2 options: <br/>
   ##### a. Classify scene context
   - cmd
       ```sh
          python scene.py [path_to_image]
       ```
   ##### b. Object detection / Brand detection
   - Follow the link to use this feature : <a href="https://github.com/SteveKhoa/hackhcmc/blob/main/main.ipynb">Follow here</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<a href="https://github.com/SteveKhoa/hackhcmc/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SteveKhoa/hackhcmc" />
</a>


Project Link: https://github.com/SteveKhoa/hackhcmc

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/SteveKhoa/hackhcmc.svg?style=for-the-badge
[forks-url]: https://github.com/SteveKhoa/hackhcmc/network
[stars-shield]: https://img.shields.io/github/stars/SteveKhoa/hackhcmc.svg?style=for-the-badge
[stars-url]: https://github.com/SteveKhoa/hackhcmc/stargazers
[issues-shield]: https://img.shields.io/github/issues/SteveKhoa/hackhcmc.svg?style=for-the-badge
[issues-url]: https://github.com/SteveKhoa/hackhcmc/issues
[Python]: http://ForTheBadge.com/images/badges/made-with-python.svg
[Python-url]: https://www.python.org/
[Git]: https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white
[VStudio]: https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
[VStudio-url]: https://code.visualstudio.com/download
[RoboFlow]: https://github.com/SteveKhoa/hackhcmc/assets/113105084/2a22de16-1abc-4b52-aa9f-ed8f9062a2a1
[RoboFlow-url]: https://roboflow.com/
[GoogleColab]: https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252
[GoogleColab-url]: https://colab.research.google.com/
