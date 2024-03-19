

# Environment Setup Guide
## Introduction
This repository provides step-by-step instructions to help you set up a Linux-based environment from scratch. Follow the guide below to build your environment and run the server.

## Requirement
Before you start, ensure that you have the following requirements settled on your Linux system:

* Ubuntu 22.04.3
* Anaconda
* Python 3.7
* Kaldi
* Firebase

* You can download the checkpoint from the [link](https://drive.google.com/drive/folders/1HFZwIK4ZuCnKVFQjH5XJ7RyViNXpcV6U?usp=drive_link). Please insert the checkpoint folder in the main folder.
* You can download the certification from the [link](https://drive.google.com/file/d/1GujDKgWTPd1mO3ZTHnpSUTM6vyX33EPW/view?usp=drive_link). It is also possible to regenerate one in firebase website. Please insert the certification file in the main folder.
## Installation
## Kaldi
Follow the instructions provided in the [Kaldi installation guide](https://medium.com/@m.chellaa/install-kaldi-asr-on-ubuntu-830418a800b5)
 to install Kaldi on your system. Once the installation is complete, proceed with the following steps:
Change the file `path.sh` in your Kaldi installation path as required for your project.

```python
KALDI_ROOT=/home/moya/kaldi   # Change to your Kaldi installation path. 

. $KALDI_ROOT/tools/config/common_path.sh
export LC_ALL=C
```

## Firebase
After setting up Firebase, you'll need to generate a new private key:

![Screenshot from 2023-09-20 17-04-05](https://github.com/Moyacaca/Speak-Slowly-Env/assets/117159970/dd282e39-b420-4f73-8229-f40f25da30c1)
1. Go to your Firebase project overview.
2. Navigate to Project Settings.
3. Select the Service Accounts tab.
4. Under the "Firebase Admin SDK" section, click the "Generate new private key" button to download the generated private key JSON file.
5. Place the private key JSON file into your project directory, typically named CNN-RNN-CTC.
Modify the path(line 17, line 26) in server.py to point to the location of the private key JSON file.

```python
cred = credentials.Certificate(
    "cgh-rcnn-flask-firebase-adminsdk-f92al-8d9038b979.json")  # Change to your private key!
save_path = 'run'
Path(save_path).mkdir(parents=True, exist_ok=True)
firebase_admin.initialize_app(
    cred, {'storageBucket': 'cgh-rcnn-flask.appspot.com'})   # connecting to firebase


def download_blob(bucket_name, filename, source_blob_name):
    credentials = service_account.Credentials.from_service_account_file(
        "cgh-rcnn-flask-firebase-adminsdk-f92al-8d9038b979.json")   # Change to your private key!
    storage_client = storage.Client(credentials=credentials)
```

## Connecting to the URL
The script titled `worker.py` has been designed to establish a connection to the specified URL. In the event that the connection is interrupted, the script is programmed to automatically attempt to re-establish the connection.
Run the URL connection using the following command:
```
python worker.py
```

## Running the Server
To run the server:

Verify that the server is configured to use port 5002 (you can change this in `server.py` if needed).
Open a terminal and navigate to your project directory.
Run the server using the following command:
```
python server.py
```
Your server should now be up and running.



## Usage
For access to the Firebase storage and additional information, please reach out to me via email at moya40930@gmail.com. Upon contact, I will grant you permission to access the storage as a collaborator.
