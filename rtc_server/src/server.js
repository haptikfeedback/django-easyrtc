const express = require('express')
const easyrtc = require('easyrtc')
const http = require('http')
const configLoader = require('./config')
const socket = require('socket.io')
const cors = require('cors')

const app = express()
app.use(cors())

const webServer = http.createServer(app)

const socketServer = socket.listen(webServer, {
    log_level: 1,
    origins: '*:*',
})

easyrtc.setOption('logLevel', 'debug')

easyrtc.events.on('easyrtcAuth', function(socket, easyrtcid, msg, socketCallback, callback) {
    easyrtc.events.defaultListeners.easyrtcAuth(socket, easyrtcid, msg, socketCallback, function(err, connectionObj){
        if (err || !msg.msgData || !msg.msgData.credential || !connectionObj) {
            callback(err, connectionObj)
            return
        }
        
        connectionObj.setField('credential', msg.msgData.credential, {'isShared':false})
        
        console.log('['+easyrtcid+'] Credential saved!', connectionObj.getFieldValueSync('credential'))
        
        callback(err, connectionObj)
    })
})

easyrtc.events.on('roomJoin', function(connectionObj, roomName, roomParameter, callback) {
    console.log('['+connectionObj.getEasyrtcid()+'] Credential retrieved!', connectionObj.getFieldValueSync('credential'))
    easyrtc.events.defaultListeners.roomJoin(connectionObj, roomName, roomParameter, callback)
})


const rtc = easyrtc.listen(app, socketServer, null, function(err, rtcRef) {
    console.log('Initiated')
    
    rtcRef.events.on('roomCreate', function(appObj, creatorConnectionObj, roomName, roomOptions, callback) {
        console.log('roomCreate fired! Trying to create: ' + roomName)

        appObj.events.defaultListeners.roomCreate(appObj, creatorConnectionObj, roomName, roomOptions, callback)
    })
})

const { server } = configLoader('development')
webServer.listen(server.port, server.host, () => {
    console.log(`Server running at ${server.host}:${server.port}...`)
})
