import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';
import './DisplayMarkdown.css'

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

                <div className="container">
                    <div className="editor">
                        <h1>Editor</h1>
                    </div>
                    <div className="preview">
                        <h1>Preview</h1>
                    </div>
                </div>
                <div class="container">
                    <div className="editor">
                        <textarea value={this.state.value} onChange={this.handleChange} cols={75} rows={60} />
                    </div>
                    <div className="preview">
                        <ReactMarkdown source={this.state.value} />
                    </div>
                </div>

            </div>
        );
    }
}

export default DisplayMarkdown;