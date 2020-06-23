import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';

class DisplayMarkdown extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ''
        };

        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.setState({value: event.target.value});
    }

    render() {
        return (
            <div>
                <textarea value={this.state.value} onChange={this.handleChange} cols={40} rows={10} />
                <div><h1>Preview</h1>
                <div><ReactMarkdown source={this.state.value} /></div>
                </div>
            </div>
        );
    }
}

export default DisplayMarkdown;