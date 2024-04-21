import './Summary.css'
import { useState, useEffect } from 'react'

import { PrimaryButtonLink, SecondaryButton, DangerButton } from '../components/Buttons'
import LoadingAnimation from '../components/Loading';

import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import BookmarkIcon from '@mui/icons-material/Bookmark';
import FlagIcon from '@mui/icons-material/Flag';

function SummarySection({ title, children }) {
    return (
        <div className='summary-section'>
            <h2>{title}</h2>
            {children}
        </div>
    )
}

function AnalysisField({ metric, pass, description }) {
    return (
        <div className='analysis-field'>
            {pass ? <CheckCircleOutlineIcon className='analysis-icon analysis-pass' /> : <HighlightOffIcon className='analysis-icon analysis-fail' />}
            <p style={{ display: 'inline', fontWeight: 700, marginRight: '0.75rem' }}>{metric}:</p>
            <p style={{ display: 'inline' }}>{description}</p>
        </div>
    )
}

function Summary() {

    const [report, setReport] = useState(null)

    useEffect(() => {
        
    })

    function handleSave() {

    }

    function handleReport() {
        
    }

    return (
        <>
            {report && (
                <div id='Summary'>
                    <div className='position-details'>
                        <h1 style={{marginBottom: '0.75rem'}}>Position Title</h1>
                        <div className='action-row'>
                            <PrimaryButtonLink href='' >Listing</PrimaryButtonLink>
                            <SecondaryButton >Save <BookmarkIcon /></SecondaryButton>
                            <DangerButton onClick={handleReport} >Report <FlagIcon /></DangerButton>
                        </div>
                        <p style={{marginTop: '1.25rem' }}>volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed velit dignissim sodales ut eu sem integer vitae justo eget magna fermentum iaculis eu non diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim tortor at auctor urna nunc id cursus metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget duis at tellus at urna condimentum mattis pellentesque id nibh tortor id aliquet lectus proin nibh nisl condimentum id venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas sed tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit</p>
                    </div>
                    <hr />
                    {/* <SummarySection title='Listing Summary' >
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </SummarySection>
                    <hr /> */}
                    <SummarySection title='Analysis Results' >
                        <AnalysisField metric='Grammar' pass={true} description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.' />
                        <AnalysisField metric='Grammar' pass={true} description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.' />
                        <AnalysisField metric='Grammar' pass={false} description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.' />
                        <AnalysisField metric='Grammar' pass={true} description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.' />
                        <AnalysisField metric='Grammar' pass={false} description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.' />
                    </SummarySection>
                    <hr />
                </div>
            )}
            {!report && (
                <div className='loading-container'>
                    <h2 style={{ marginBottom: '3.5rem' }}>Fetching Analysis</h2>
                    <LoadingAnimation />
                </div>
            )}
        </>
    )
}

export default Summary