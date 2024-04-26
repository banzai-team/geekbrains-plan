import React, {ReactNode} from "react";
import {Outlet} from "react-router-dom";
import {HeartCrack} from "lucide-react";

import Sidebar from "~/components/Sidebar";
import Header from "~/components/Header";
import {Spinner} from "~/components/ui/spinner";

type EmptyProps = {
    text: string;
    icon?: ReactNode;
    children?: any;
}

const Empty: React.FC<EmptyProps> = ({text, icon, children}) => {
    return (
        <div className="flex w-full flex-col py-20 justify-center items-center">
            { icon ? icon : (<HeartCrack className="w-16 h-16 text-primary"/>)}
            <div className="text-xl pt-5">{text}</div>
            {children}
        </div>
    )
}


export default Empty;