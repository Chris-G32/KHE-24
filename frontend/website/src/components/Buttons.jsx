import './Buttons.css'

import LaunchIcon from '@mui/icons-material/Launch';

function PrimaryButton({ onClick, children, style }) {
    return (
        <button className='btn primary-btn' onClick={onClick} style={style}>{children}</button>
    )    
}

function SecondaryButton({ onClick, children, style }) {
    return (
        <button className='btn secondary-btn' onClick={onClick} style={style} >{children}</button>
    )
}

function DangerButton({ onClick, children, style }) {
    return (
        <button className='btn danger-btn' onClick={onClick} style={style}>{children}</button>
    )    
}

function PrimaryButtonLink({ href, children, style }) {
    return (
        <a className='btn-link primary-btn-link' href={href} style={style}>{children}<LaunchIcon /></a>
    ) 
}

function SecondaryButtonLink({ href, children, style }) {
    return (
        <a className='btn-link secondary-btn-link' href={href} style={style}>{children}<LaunchIcon /></a>
    )
}

function DisabledButton({ children }) {
    return (
        <button className='disabled-btn btn' disabled>{children}</button>
    )
}

export {
    PrimaryButton,
    PrimaryButtonLink,
    SecondaryButton,
    SecondaryButtonLink,
    DangerButton,
    DisabledButton
}