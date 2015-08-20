---
layout: default
comments: true
category: tools
tags: [android]
title: Deploy Environment for Android Map Development
---
---

The following suggestions are all based on Windows. It should be similar on Mac.

Reference Google document from [here](https://developers.google.com/maps/documentation/android/signup) and [here](https://developers.google.com/maps/documentation/android/start).

## Get map key from Google

### Get package name

For Eclipse, open **Androidmanifast.xml** and the package name is:

![003_package_name_in_Eclipse](../images/003_package_name_in_Eclipse.png)

For Android Studio, **TODO**

### Get SHA1 fingerprint certificate

For Eclipse, go to **Windows -> Preferences -> Android -> Build** to find it.

For Android Studio, go to your java bin directory, and run:

    keytool -list -v -keystore c:\users\<your_user_name>\.android\debug.keystore -alias androiddebugkey -storepass android -keypass android

You will get your SHA1 fingerprint from:

![004_SHA1_in_Android_Studio](../images/004_SHA1_in_Android_Studio.png)

### Generate the key

With your package name and SHA1 fingerprint, go to []() to generate your key.

1. Go to the Google Developers Console.
2. In the sidebar on the left, select Credentials.
3. If your project doesn't already have an Android API key, create one now by selecting **Add credentials -> API key -> Android key**.
4. In the resulting dialog, enter your app's SHA-1 fingerprint and package name. For example:
5. Your new Android API key appears in the list of API keys for your project. An API key is a string of characters, something like this:
    AIzaSyBdVl-cTICSwYKrZ95SuvNw7dbMuDt1KG0

If you want to use an existing key, open it, and `add package name and fingerprint`, and add your package name and fingerprint.

### Add the Android API key to your application

For Eclipse, in `AndroidManifest.xml`, add the following element as a child of the `<application>` element. Take the following as an example:

![002_add_key_in_Eclipse](../images/002_add_key_in_Eclipse.png)

For Android Studio, in res/values/google_maps_api.xml, add your Android API key as the value of `google_maps_key` element.

## Install Google Service in Genymotion VM

Genymotion is a Virtual Android Environment built on x86 and Virtualbox. It's not an ARM emulator so it's performance is way better than the Android SDK Emulator. However in their latest update they've removed both ARM Translation and Google Play Apps. 

We need to install the above two functions for genymotion VM first.

In order to install ARM translation for Genymotion, follow these steps:

1. Download the zip file from [here](http://filetrip.net/dl?4SUOrdcMRv)
2. Open Genymotion and go to the home screen.
3. Drag and Drop the .zip file onto the Genymotion window.
4. Restart Genymotion

Genymotion can now run applications that require ARM emulation.

It is similar for Google Play Apps, which can be downloaded from [here](https://www.androidfilehost.com/?fid=95784891001614559)

Go to [How to install Google Play Services in a Genymotion VM (with no drag and drop support)?](http://stackoverflow.com/questions/20121883/how-to-install-google-play-services-in-a-genymotion-vm-with-no-drag-and-drop-su) for details.