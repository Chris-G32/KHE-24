import './Summary.css'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

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

    const { reportId } = useParams()
    console.log(reportId)

    useEffect(() => {
        const getReport = async () => {
            const url = `${import.meta.env.VITE_API_URL}/report?report_id=${reportId}`
            const response = await axios.get(url)
            setReport(response.data)

            console.log(response)
        }
        getReport()
    }, [])

    function handleSave() {

    }

    function handleReport() {
        
    }

    return (
        <>
            {report && (
                <div id='Summary'>
                    <div className='position-details'>
                        <h1 style={{marginBottom: '0.75rem'}}>{report.job.position_title}</h1>
                        <div className='action-row'>
                            <PrimaryButtonLink href={report.job.link} >Listing</PrimaryButtonLink>
                            <SecondaryButton >Save <BookmarkIcon /></SecondaryButton>
                            <DangerButton onClick={handleReport} >Report <FlagIcon /></DangerButton>
                        </div>
                        <p style={{marginTop: '1.25rem' }}>{report.result.ai_summary}</p>
                    </div>
                    <hr />
                    {/* <SummarySection title='Listing Summary' >
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </SummarySection>
                    <hr /> */}
                    <SummarySection title='Analysis Results' >
                        <AnalysisField metric='Suspicious Email' pass={!report.result.email_suspicious} description='Is the email suspicious' />
                        <AnalysisField metric='Suspicious Phone' pass={!report.result.phone_suspicious} description='Is the phone number suspicious' />
                        <AnalysisField metric='Suspicious Link' pass={!report.result.link_suspicious} description='Is the link suspicious' />
                        <AnalysisField metric='Grammar' pass={report.result.grammar_error_count > 3 ? false : true} description='Were there a lot of grammar mistakes' />
                        <AnalysisField metric='Spelling' pass={report.result.spelling_error_count > 3 ? false : true} description='Were there a lot of spelling mistakes' />
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