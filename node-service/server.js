const express = require("express")
const app = express()

const PORT = 3000

app.get("/",(req, res)=>{
    res.send("Welcom to the base of the node data pipeline service worker")
})
app.get("/ingest",(req, res)=>{
    res.send("Here we lookup data registered inside the kafka message broker and process them before storing them in a permanent db")
})


app.listen(PORT, ()=>{
    console.log(`Node service worker running and listening on port ${PORT}`)
})