import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";
import Alert from "@material-ui/lab/Alert";
import AppBar from 'material-ui/AppBar';
//import DropDownMenu from 'material-ui/DropDownMenu';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MenuItem from 'material-ui/MenuItem';
import axios from "axios";
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel'

const useStyles = makeStyles((theme) => ({
  input: {
    margin: 5,
  },
}));

export default function RunSubmitForm() {
  const url = "/api/submit";
  const [success, setSuccess] = useState(undefined);
  const [system, setSystem] = useState({index: 1});


  function handleSelectSystem(e) {
    setSystem({ ...system, index: e.target.value });
  }

  function pageControl(){
    if( system.index === 1){
      return (
        <div><h3>Kundur</h3></div>
      );
    } else if( system.index === 2) {
      return (
        <div><h3>IEEE14</h3></div>
      );
    } else if( system.index === 3) {
      return (
        <div><h3>WECC</h3></div>
      );
    }
  }

  function handleSubmit(e) {
    e.preventDefault();
    const data = new FormData();
    //data.set("firstName", identity.firstName);
    //data.set("lastName", identity.lastName);
    //data.set("job", job);
    data.set("systemIndex", system.index);

    axios({
      method: "post",
      url: url,
      data: data,
    })
      .then(function (response) {
        console.log(response);
        setSuccess(true);
      })
      .catch(function (response) {
        setSuccess(false);
        console.log(response);
      });
  }

  function Alerting() {
    if (success === true) {
      return <Alert severity="success">Data sucessfully sent !</Alert>;
    } else if (success === false) {
      return <Alert severity="error">Oops. An error just occurred!</Alert>;
    } else {
      return null;
    }
  }

  return (
    <Container>
      <form onSubmit={handleSubmit}>
        <MuiThemeProvider>
        <AppBar
            title="An Elastic Parallel Computing Cluster Demo &ndash; by IEEE PES Task Force 'Cloud4PowerGrid'"
            style={
              {
                background:"#ffb400" //hex color values (yellow)
              }
            }
            titleStyle = {
              {
                color:"#FFFFF" //color of text (black)
              }
            }
            showMenuIconButton={false}
         />
         <br/><br/><br/>
         <Typography align="center">
         <h2> Select A System for Time-domain Study (TDS) </h2>
         <br/><br/>
         <InputLabel id="study-system-select-label">Study System</InputLabel>
         <Select sx={{m:5, minWidth:100}}
          labelId="study-system-select-label"
          value={system.index}
          label="Study System"
          onChange={handleSelectSystem}
         >

          <MenuItem value={1}>Kundur's System</MenuItem>
          <MenuItem value={2}>IEEE14 Bus System</MenuItem>
          <MenuItem value={3}>WECC System</MenuItem>

        </Select>
        </Typography>
        <br/><br/><br/>
        <Typography align="center">
        {pageControl()}
        </Typography>
        <br/><br/><br/>
        <Typography align="center">
              <Button type="submit" color="primary" variant="contained">
                Submit Run
              </Button>
              <div style={{ marginTop: 10 }}></div>
              <Button href="../" color="primary" variant="outlined">
                 Return Home
              </Button>
              &nbsp;&nbsp;&nbsp;
              <Button href="../rundata" color="primary" variant="outlined">
                 Check Results
              </Button>
              &nbsp;&nbsp;&nbsp;
              <Button href="../grafana" color="primary" variant="outlined">
                 Run Monitoring
              </Button>
              <div style={{ marginTop: 10 }}>
                <Alerting></Alerting>
              </div>
        </Typography>
        </MuiThemeProvider>
      </form>
    </Container>
  );
}

