import React from "react";
import {Home, LineChart, BookMarked, BookOpenCheck, Settings, ShoppingCart, Users2} from "lucide-react";
import {Tooltip, TooltipContent, TooltipProvider, TooltipTrigger} from "~/components/ui/tooltip";
import {NavLink, Link} from "react-router-dom";

export const menuItems = [
    {
        text: "Главная",
        icon: <Home className="h-5 w-5" />,
        link: "/",
    },
    {
        text: "Курсы",
        icon: <BookMarked className="h-5 w-5" />,
        link: "/lecture",
    },
    {
        text: "Настройки",
        icon: <Settings className="h-5 w-5" />,
        link: "/settings",
    },
];

const Sidebar: React.FC = () => {
    return (
        <aside className="fixed inset-y-0 left-0 z-10 hidden w-14 flex-col border-r bg-background sm:flex">
            <nav className="flex flex-col items-center gap-4 px-2 sm:py-5">
                <Link
                    to="/"
                    className="group flex h-9 w-9 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-lg font-semibold text-primary-foreground md:h-8 md:w-8 md:text-base"
                >
                    <BookOpenCheck className="h-4 w-4 transition-all group-hover:scale-110" />
                    <span className="sr-only">Acme Inc</span>
                </Link>
                {
                    menuItems.map((item, key) => (
                        <TooltipProvider key={`menu-item-${key}`}>
                            <Tooltip>
                                <TooltipTrigger asChild>
                                    <NavLink
                                        to={item.link}
                                        isActive={true}
                                        className="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"

                                        // className={({ isActive }: {isActive: any}) => isActive ? "bg-zinc-950" : "flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"}
                                        // className={({ isActive, isPending, isTransitioning }) =>
                                        //     [
                                        //         "flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8",
                                        //         isActive ? "bg-zinc-950" : "",
                                        //     ].join(" ")
                                        // }
                                    >
                                        {item.icon}
                                        <span className="sr-only">{item.text}</span>
                                    </NavLink>
                                </TooltipTrigger>
                                <TooltipContent side="right">{item.text}</TooltipContent>
                            </Tooltip>
                        </TooltipProvider>
                    ))
                }
            </nav>
        </aside>
    );
};

export default Sidebar;