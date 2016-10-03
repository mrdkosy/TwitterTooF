#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    osc.setup(6667);
}

//--------------------------------------------------------------
void ofApp::update(){
    
    vector<string> message;
     while(osc.hasWaitingMessages()){
         ofxOscMessage msg;
         osc.getNextMessage(msg);
         if(msg.getAddress() == "/tweet"){
             string m = msg.getArgAsString(0);
             cout << m << endl;
             message.push_back(m);
         }
     }
}

//--------------------------------------------------------------
void ofApp::draw(){

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
